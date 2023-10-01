import check50
import check50.py
import check50.flask
import os


# Set API_KEY to a dummy value. The distro code looks at this value, but it's not used in checks.
os.environ["API_KEY"] = "foo"


@check50.check()
def exists():
    """app.py existe"""
    check50.exists("app.py")
    check50.include("lookup.py")
    check50.py.append_code("helpers.py", "lookup.py")


@check50.check(exists)
def startup():
    """la aplicación se inicia"""
    Finance().get("/").status(200)


@check50.check(startup)
def register_page():
    """La página de registro tiene todos los elementos requeridos."""
    Finance().validate_form("/register", ["username", "password", "confirmation"])


@check50.check(register_page)
def simple_register():
    """registro de usuario exitoso"""
    Finance().register("_cs50", "ohHai28!", "ohHai28!").status(200)


@check50.check(register_page)
def register_empty_field_fails():
    """el registro con un campo vacío falla"""
    for user in [("", "crimson", "crimson"), ("jharvard", "crimson", ""), ("jharvard", "", "")]:
        Finance().register(*user).status(400)


@check50.check(register_page)
def register_password_mismatch_fails():
    """registro con contraseña no coincidente falla"""
    Finance().register("check50user1", "thisiscs50", "crimson").status(400)


@check50.check(register_page)
def register_reject_duplicate_username():
    """el registro rechaza nombre de usuario duplicado"""
    user = ["elfie", "Doggo28!", "Doggo28!"]
    Finance().register(*user).status(200).register(*user).status(400)


@check50.check(startup)
def login_page():
    """La página de inicio de sesión tiene todos los elementos requeridos."""
    if Finance().page_exists("/signin"):
        Finance().validate_form("/signin", ["username", "password"])
        return
    Finance().validate_form("/login", ["username", "password"])


@check50.check(simple_register)
def can_login():
    """iniciar sesión como usuario registrado tiene éxito"""
    Finance().login("_cs50", "ohHai28!").status(200).get("/", follow_redirects=False).status(200)


@check50.check(can_login)
def quote_page():
    """La página de cotización tiene todos los elementos requeridos."""
    Finance().login("_cs50", "ohHai28!").validate_form("/quote", "symbol")


@check50.check(quote_page)
def quote_handles_invalid():
    """la cotización maneja el símbolo de cotización no válido"""
    Finance().login("_cs50", "ohHai28!").quote("ZZZ").status(400)


@check50.check(quote_page)
def quote_handles_blank():
    """la cotización maneja el símbolo de cotización en blanco"""
    Finance().login("_cs50", "ohHai28!").quote("").status(400)


@check50.check(quote_page)
def quote_handles_valid():
    """la cotización maneja el símbolo de cotización válido"""
    (Finance().login("_cs50", "ohHai28!")
              .quote("AAAA")
              .status(200)
              .content(r"28\.00", "28.00", name="body"))


@check50.check(can_login)
def buy_page():
    """la página de compra tiene todos los elementos requeridos"""
    Finance().login("_cs50", "ohHai28!").validate_form("/buy", ["shares", "symbol"])


@check50.check(buy_page)
def buy_handles_invalid():
    """comprar maneja el símbolo de cotización no válido"""
    Finance().login("_cs50", "ohHai28!").transaction("/buy", "ZZZZ", "2").status(400)


@check50.check(buy_page)
def buy_handles_incorrect_shares():
    """comprar maneja acciones fraccionarias, negativas y no-numéricas"""
    (Finance().login("_cs50", "ohHai28!")
              .transaction("/buy", "AAAA", "-1").status(400)
              .transaction("/buy", "AAAA", "1.5").status(400)
              .transaction("/buy", "AAAA", "foo").status(400))


@check50.check(buy_page)
def buy_handles_valid():
    """comprar maneja compra valida"""
    (Finance().login("_cs50", "ohHai28!")
              .transaction("/buy", "AAAA", "4")
              .content(r"112\.00", "112.00")
              .content(r"9,?888\.00", "9,888.00"))


@check50.check(buy_handles_valid)
def sell_page():
    """la página de venta tiene todos los elementos requeridos"""
    (Finance().login("_cs50", "ohHai28!")
              .validate_form("/sell", ["shares"])
              .validate_form("/sell", ["symbol"], field_tag="select"))


@check50.check(buy_handles_valid)
def sell_handles_invalid():
    """vender maneja un número no válido de acciones"""
    Finance().login("_cs50", "ohHai28!").transaction("/sell", "AAAA", "8").status(400)


@check50.check(buy_handles_valid)
def sell_handles_valid():
    """vender maneja venta válida"""
    (Finance().login("_cs50", "ohHai28!")
              .transaction("/sell", "AAAA", "2")
              .content(r"56\.00", "56.00")
              .content(r"9,?944\.00", "9,944.00"))



class Finance(check50.flask.app):
    """Extensión de la clase flask.App que agrega funciones específicas de Finanzas"""

    APP_NAME = "app.py"

    def __init__(self):
        """función auxiliar para registrar usuarios"""
        super().__init__(self.APP_NAME)

    def register(self, username, password, confirmation):
        """registrar nuevo usuario"""
        form = {"username": username, "password": password, "confirmation": confirmation}
        return self.post("/register", data=form)

    def login(self, username, password):
        """función auxiliar para iniciar sesión"""
        route = "/login"
        if self.page_exists("/signin"):
            route = "/signin"
        return self.post(route, data={"username": username, "password": password})

    def quote(self, ticker):
        """Consultar aplicación para obtener una cotización para 'ticker'"""
        return self.post("/quote", data={"symbol": ticker})

    def transaction(self, route, symbol, shares):
        """Enviar solicitud a 'route' ('/buy' o '/sell') para realizar la transacción relevante"""
        return self.post(route, data={"symbol": symbol, "shares": shares})

    def validate_form(self, route, fields, field_tag="input"):
        """Asegúrese de que el formulario HTML en 'route' tenga campos de entrada proporcionados por 'fields'"""
        if not isinstance(fields, list):
            fields = [fields]

        content = self.get(route).content()
        required = {field: False for field in fields}
        for tag in content.find_all(field_tag):
            try:
                name = tag.attrs["name"]
                if required[name]:
                    raise Error("se encontró más de un campo llamado \"{}\"".format(name))
            except KeyError:
                pass
            else:
                check50.log("se encontró campo \"{}\" requerido".format(name))
                required[name] = True

        try:
            missing = next(name for name, found in required.items() if not found)
        except StopIteration:
            pass
        else:
            raise check50.Failure(f"se esperó encontrar el campo {field_tag} con el nombre \"{missing}\", pero no fue hallado")

        if content.find("button", type="submit") is None:
            raise check50.Failure("se esperó encontrar el botón para enviar formulario (submit form), pero no fue hallado")

        return self

    def page_exists(self, route):
        return self.get(route).status() == 200
