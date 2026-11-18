import check50

USO = "Uso: python adn.py data.csv secuencia.txt [informe.txt]"


def informe(nombre, porcentaje, analizados, coincidentes, nivel):
    """The exact report the handout asks for / El informe exacto que pide el enunciado"""
    return (
        "Coincidencia encontrada:\n"
        f"Nombre            : {nombre}\n"
        f"Coincidencia STR  : {porcentaje}%\n"
        f"STRs analizados   : {analizados}\n"
        f"STRs coincidentes : {coincidentes}\n"
        f"Nivel de confianza: {nivel}\n"
    )


def limpio(texto):
    """Spaces at the end of a line and blank lines at the end do not count / No cuentan los espacios al final"""
    lineas = [linea.rstrip() for linea in texto.replace("\r\n", "\n").split("\n")]
    while lineas and not lineas[-1]:
        lineas.pop()
    return "\n".join(lineas)


def comparar(comando, esperada, ayuda=None):
    salida = check50.run(comando).stdout(timeout=10)
    if limpio(salida) != limpio(esperada):
        raise check50.Mismatch(esperada, salida, help=ayuda)


@check50.check()
def exists():
    """adn.py existe"""
    check50.exists("adn.py")
    check50.include("basesdedatos", "secuencias", "pruebas")


@check50.check(exists)
def uso_sin_argumentos():
    """muestra el mensaje de uso si no se pasan argumentos"""
    comparar("python3 adn.py", USO + "\n")


@check50.check(exists)
def uso_un_argumento():
    """muestra el mensaje de uso si se pasa solo un argumento"""
    comparar("python3 adn.py basesdedatos/pequeno.csv", USO + "\n")


@check50.check(exists)
def uso_cuatro_argumentos():
    """muestra el mensaje de uso si se pasan cuatro argumentos"""
    comparar("python3 adn.py basesdedatos/pequeno.csv secuencias/1.txt informe.txt extra.txt", USO + "\n")


@check50.check(exists)
def secuencia1():
    """identifica correctamente secuencias/1.txt (Jose Maria Vargas, 100.00%, Alto)"""
    comparar("python3 adn.py basesdedatos/pequeno.csv secuencias/1.txt",
             informe("Jose Maria Vargas", "100.00", 3, 3, "Alto"))


@check50.check(exists)
def secuencia2():
    """identifica correctamente secuencias/2.txt (Jose Maria Vargas, 33.33%, Bajo)"""
    comparar("python3 adn.py basesdedatos/pequeno.csv secuencias/2.txt",
             informe("Jose Maria Vargas", "33.33", 3, 1, "Bajo"))


@check50.check(exists)
def secuencia3():
    """identifica correctamente secuencias/3.txt (Cecilio Acosta, 66.67%, Bajo)"""
    comparar("python3 adn.py basesdedatos/pequeno.csv secuencias/3.txt",
             informe("Cecilio Acosta", "66.67", 3, 2, "Bajo"))


@check50.check(exists)
def secuencia4():
    """identifica correctamente secuencias/4.txt (Romulo Gallegos, 100.00%, Alto)"""
    comparar("python3 adn.py basesdedatos/pequeno.csv secuencias/4.txt",
             informe("Romulo Gallegos", "100.00", 3, 3, "Alto"))


@check50.check(exists)
def secuencia5():
    """identifica correctamente secuencias/5.txt (Jose Antonio Paez, 100.00%, Alto)"""
    comparar("python3 adn.py basesdedatos/grande.csv secuencias/5.txt",
             informe("Jose Antonio Paez", "100.00", 8, 8, "Alto"))


@check50.check(exists)
def secuencia6():
    """identifica correctamente secuencias/6.txt (Santiago Marino, 100.00%, Alto)"""
    comparar("python3 adn.py basesdedatos/grande.csv secuencias/6.txt",
             informe("Santiago Marino", "100.00", 8, 8, "Alto"))


@check50.check(exists)
def secuencia7():
    """identifica correctamente secuencias/7.txt (Luisa Caceres de Arismendi, 100.00%, Alto)"""
    comparar("python3 adn.py basesdedatos/grande.csv secuencias/7.txt",
             informe("Luisa Caceres de Arismendi", "100.00", 8, 8, "Alto"))


@check50.check(exists)
def secuencia8():
    """identifica correctamente secuencias/8.txt (Andres Bello, 100.00%, Alto)"""
    comparar("python3 adn.py basesdedatos/grande.csv secuencias/8.txt",
             informe("Andres Bello", "100.00", 8, 8, "Alto"))


@check50.check(exists)
def secuencia9():
    """identifica correctamente secuencias/9.txt (Josefa Camejo, 100.00%, Alto)"""
    comparar("python3 adn.py basesdedatos/grande.csv secuencias/9.txt",
             informe("Josefa Camejo", "100.00", 8, 8, "Alto"))


@check50.check(exists)
def secuencia10():
    """identifica correctamente secuencias/10.txt (Simon Bolivar, 100.00%, Alto)"""
    comparar("python3 adn.py basesdedatos/grande.csv secuencias/10.txt",
             informe("Simon Bolivar", "100.00", 8, 8, "Alto"))


@check50.check(exists)
def secuencia11():
    """identifica correctamente secuencias/11.txt (Francisco de Miranda, 100.00%, Alto)"""
    comparar("python3 adn.py basesdedatos/grande.csv secuencias/11.txt",
             informe("Francisco de Miranda", "100.00", 8, 8, "Alto"))


@check50.check(exists)
def secuencia12():
    """identifica correctamente secuencias/12.txt (Luis Brion, 100.00%, Alto)"""
    comparar("python3 adn.py basesdedatos/grande.csv secuencias/12.txt",
             informe("Luis Brion", "100.00", 8, 8, "Alto"))


@check50.check(exists)
def secuencia13():
    """identifica correctamente secuencias/13.txt (Francisco de Miranda, 12.50%, Bajo)"""
    comparar("python3 adn.py basesdedatos/grande.csv secuencias/13.txt",
             informe("Francisco de Miranda", "12.50", 8, 1, "Bajo"),
             ayuda="varias personas empatan con 1 STR coincidente; debe reportarse la que aparece primero en el CSV")


@check50.check(exists)
def secuencia14():
    """identifica correctamente secuencias/14.txt (Simon Rodriguez, 100.00%, Alto)"""
    comparar("python3 adn.py basesdedatos/grande.csv secuencias/14.txt",
             informe("Simon Rodriguez", "100.00", 8, 8, "Alto"))


@check50.check(exists)
def secuencia15():
    """identifica correctamente secuencias/15.txt (Carlos Soublette, 100.00%, Alto)"""
    comparar("python3 adn.py basesdedatos/grande.csv secuencias/15.txt",
             informe("Carlos Soublette", "100.00", 8, 8, "Alto"))


@check50.check(exists)
def secuencia16():
    """identifica correctamente secuencias/16.txt (Luis Brion, 12.50%, Bajo)"""
    comparar("python3 adn.py basesdedatos/grande.csv secuencias/16.txt",
             informe("Luis Brion", "12.50", 8, 1, "Bajo"),
             ayuda="varias personas empatan con 1 STR coincidente; debe reportarse la que aparece primero en el CSV")


@check50.check(exists)
def secuencia17():
    """identifica correctamente secuencias/17.txt (Antonio Jose de Sucre, 100.00%, Alto)"""
    comparar("python3 adn.py basesdedatos/grande.csv secuencias/17.txt",
             informe("Antonio Jose de Sucre", "100.00", 8, 8, "Alto"))


@check50.check(exists)
def secuencia18():
    """identifica correctamente secuencias/18.txt (Antonio Jose de Sucre, 87.50%, Medio)"""
    comparar("python3 adn.py basesdedatos/grande.csv secuencias/18.txt",
             informe("Antonio Jose de Sucre", "87.50", 8, 7, "Medio"))


@check50.check(exists)
def secuencia19():
    """identifica correctamente secuencias/19.txt (Jose Felix Ribas, 100.00%, Alto)"""
    comparar("python3 adn.py basesdedatos/grande.csv secuencias/19.txt",
             informe("Jose Felix Ribas", "100.00", 8, 8, "Alto"))


@check50.check(exists)
def secuencia20():
    """identifica correctamente secuencias/20.txt (Rafael Urdaneta, 12.50%, Bajo)"""
    comparar("python3 adn.py basesdedatos/grande.csv secuencias/20.txt",
             informe("Rafael Urdaneta", "12.50", 8, 1, "Bajo"))


@check50.check(exists)
def sin_coincidencia():
    """imprime "Sin coincidencia" si ningun STR coincide con nadie"""
    comparar("python3 adn.py pruebas/sin_coincidencia.csv secuencias/10.txt", "Sin coincidencia\n")


@check50.check(exists)
def empate():
    """en un empate reporta a la persona que aparece primero en el CSV"""
    comparar("python3 adn.py pruebas/empate.csv secuencias/10.txt",
             informe("Manuel Palacio Fajardo", "50.00", 8, 4, "Bajo"),
             ayuda="dos personas tienen 4 STRs coincidentes; gana la que aparece primero en el archivo")


@check50.check(exists)
def nivel_medio():
    """asigna el nivel Medio a una coincidencia de 75%"""
    comparar("python3 adn.py pruebas/medio.csv secuencias/10.txt",
             informe("Cristobal Mendoza", "75.00", 8, 6, "Medio"))


@check50.check(exists)
def guarda_informe():
    """guarda en el tercer argumento una copia exacta del informe"""
    esperada = informe("Antonio Jose de Sucre", "87.50", 8, 7, "Medio")
    comparar("python3 adn.py basesdedatos/grande.csv secuencias/18.txt informe.txt", esperada)
    check50.exists("informe.txt")
    with open("informe.txt") as archivo:
        guardado = archivo.read()
    if limpio(guardado) != limpio(esperada):
        raise check50.Mismatch(esperada, guardado, help="el archivo informe.txt no tiene el mismo informe que la pantalla")


@check50.check(exists)
def no_guarda_sin_tercer_argumento():
    """no crea ningun archivo si no se da el tercer argumento"""
    import os
    antes = set(os.listdir("."))
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/5.txt").stdout(timeout=10)
    nuevos = set(os.listdir(".")) - antes - {"__pycache__"}
    if nuevos:
        raise check50.Failure("se crearon archivos que no se pidieron: " + ", ".join(sorted(nuevos)))
