import check50
import check50.c

# check50 de Tarjetas de Débito (CI-2126, sept-dic 2026).
# Debit-card checker tests (CI-2126, Sep-Dec 2026).
#
# Cada prueba le pasa un número al programa y verifica que la última línea sea
# exactamente VISA DEBITO, CIRRUS, DISCOVER DEBITO, MAESTRO o INVALIDO.
# Each test feeds one card number and expects exactly one of those labels.
#
# Hay cuatro familias de pruebas / Four families of tests:
#   1. Tarjetas válidas de cada marca, incluyendo longitudes límite (12, 13, 15, 19).
#      Valid cards per brand, including edge lengths.
#   2. Prefijo y longitud correctos pero Luhn incorrecto: solo un programa que
#      realmente aplica Luhn las rechaza.
#      Right prefix and length but wrong checksum: only a real Luhn check rejects them.
#   3. Luhn correcto pero longitud que la marca no admite.
#      Valid checksum but a length the brand does not allow.
#   4. Prefijos que no son de débito según el enunciado (otros números, AMEX, etc.).
#      Prefixes that are not debit prefixes per the assignment.


def esperar(numero, salida):
    """Ejecuta ./debito con un número y exige la salida indicada como última línea.
    Runs ./debito with one number and requires that exact final output."""
    check50.run("./debito").stdin(numero).stdout(salida + "\n").stdout(check50.EOF).exit(0)


@check50.check()
def exists():
    """debito.c existe"""
    check50.exists("debito.c")


@check50.check(exists)
def compiles():
    """debito.c compila"""
    check50.c.compile("debito.c", lcs50=True)


# ---------- 1. Tarjetas válidas / valid cards ----------

@check50.check(compiles)
def test1():
    """identifica 4400002000000004 como VISA DEBITO"""
    esperar("4400002000000004", "VISA DEBITO")


@check50.check(compiles)
def test2():
    """identifica 4508000000000009 como VISA DEBITO"""
    esperar("4508000000000009", "VISA DEBITO")


@check50.check(compiles)
def test3():
    """identifica 4026104332185 (13 dígitos) como VISA DEBITO"""
    esperar("4026104332185", "VISA DEBITO")


@check50.check(compiles)
def test4():
    """identifica 4026104332181967897 (19 dígitos) como VISA DEBITO"""
    esperar("4026104332181967897", "VISA DEBITO")


@check50.check(compiles)
def test5():
    """identifica 5105105105105100 como MASTERCARD DEBITO (CIRRUS)"""
    esperar("5105105105105100", "CIRRUS")


@check50.check(compiles)
def test6():
    """identifica 5555555555554444 como MASTERCARD DEBITO (CIRRUS)"""
    esperar("5555555555554444", "CIRRUS")


@check50.check(compiles)
def test7():
    """identifica 6500000000000002 como DISCOVER DEBITO"""
    esperar("6500000000000002", "DISCOVER DEBITO")


@check50.check(compiles)
def test8():
    """identifica 6011000000000004 como DISCOVER DEBITO"""
    esperar("6011000000000004", "DISCOVER DEBITO")


@check50.check(compiles)
def test9():
    """identifica 5038104332181960 como MAESTRO"""
    esperar("5038104332181960", "MAESTRO")


@check50.check(compiles)
def test10():
    """identifica 6762990000000007 como MAESTRO"""
    esperar("6762990000000007", "MAESTRO")


@check50.check(compiles)
def test11():
    """identifica 501870726848 (12 dígitos) como MAESTRO"""
    esperar("501870726848", "MAESTRO")


@check50.check(compiles)
def test12():
    """identifica 503896198909015 (15 dígitos) como MAESTRO"""
    esperar("503896198909015", "MAESTRO")


@check50.check(compiles)
def test13():
    """identifica 5018707268484920000 (19 dígitos) como MAESTRO"""
    esperar("5018707268484920000", "MAESTRO")


# ---------- 2. Luhn incorrecto / wrong checksum ----------

@check50.check(compiles)
def test14():
    """identifica 4400002000000005 como INVALIDO (prefijo y longitud VISA válidos, checksum inválido)"""
    esperar("4400002000000005", "INVALIDO")


@check50.check(compiles)
def test15():
    """identifica 5105105105105106 como INVALIDO (prefijo y longitud CIRRUS válidos, checksum inválido)"""
    esperar("5105105105105106", "INVALIDO")


@check50.check(compiles)
def test16():
    """identifica 6011000000000005 como INVALIDO (prefijo y longitud DISCOVER válidos, checksum inválido)"""
    esperar("6011000000000005", "INVALIDO")


@check50.check(compiles)
def test17():
    """identifica 5038104332181961 como INVALIDO (prefijo y longitud MAESTRO válidos, checksum inválido)"""
    esperar("5038104332181961", "INVALIDO")


# ---------- 3. Longitud no admitida / wrong length ----------

@check50.check(compiles)
def test18():
    """identifica 402610433218104 como INVALIDO (prefijo VISA y checksum válidos, 15 dígitos)"""
    esperar("402610433218104", "INVALIDO")


@check50.check(compiles)
def test19():
    """identifica 510510510510515 como INVALIDO (prefijo CIRRUS y checksum válidos, 15 dígitos)"""
    esperar("510510510510515", "INVALIDO")


@check50.check(compiles)
def test20():
    """identifica 601100000000001 como INVALIDO (prefijo DISCOVER y checksum válidos, 15 dígitos)"""
    esperar("601100000000001", "INVALIDO")


@check50.check(compiles)
def test21():
    """identifica 4062901840 como INVALIDO (longitud y dígitos identificadores inválidos)"""
    esperar("4062901840", "INVALIDO")


@check50.check(compiles)
def test22():
    """identifica 430000000000000 como INVALIDO (dígitos identificadores VISA, longitud AMEX inválidos)"""
    esperar("430000000000000", "INVALIDO")


# ---------- 4. Prefijos que no son de débito / non-debit prefixes ----------

@check50.check(compiles)
def test23():
    """identifica 1234567890 como INVALIDO (longitud, checksum, dígitos identificadores inválidos)"""
    esperar("1234567890", "INVALIDO")


@check50.check(compiles)
def test24():
    """identifica 369421438430814 como INVALIDO (dígitos identificadores inválidos)"""
    esperar("369421438430814", "INVALIDO")


@check50.check(compiles)
def test25():
    """identifica 5673598276138003 como INVALIDO (dígitos identificadores inválidos)"""
    esperar("5673598276138003", "INVALIDO")


@check50.check(compiles)
def test26():
    """identifica 4111111111111113 como INVALIDO (dígitos identificadores y checksum inválidos)"""
    esperar("4111111111111113", "INVALIDO")


@check50.check(compiles)
def test27():
    """identifica 4222222222223 como INVALIDO (dígitos identificadores y checksum inválidos)"""
    esperar("4222222222223", "INVALIDO")


@check50.check(compiles)
def test28():
    """identifica 3400000000000620 como INVALIDO (dígitos identificadores AMEX, longitud VISA/Mastercard inválidos)"""
    esperar("3400000000000620", "INVALIDO")


@check50.check(compiles)
def test29():
    """identifica 4111111111111111 como INVALIDO (checksum válido, pero 4111 no es prefijo de VISA DEBITO)"""
    esperar("4111111111111111", "INVALIDO")


@check50.check(compiles)
def test30():
    """identifica 2221000000000009 como INVALIDO (checksum válido, rango 2221-2720 excluido del problema)"""
    esperar("2221000000000009", "INVALIDO")
