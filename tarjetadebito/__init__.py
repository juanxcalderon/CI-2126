import check50
import check50.c

@check50.check()
def exists():
    """debito.c existe"""
    check50.exists("debito.c")

@check50.check(exists)
def compiles():
    """debito.c compila"""
    check50.c.compile("debito.c", lcs50=True)

@check50.check(compiles)
def test1():
    """identifica 4400002000000004 como VISA DEBITO"""
    check50.run("./debito").stdin("4400002000000004").stdout("VISA DEBITO\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test2():
    """identifica 4508000000000000 como VISA DEBITO"""
    check50.run("./debito").stdin("4508000000000000").stdout("VISA DEBITO\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test3():
    """identifica 5105105105105100 como MASTERCARD DEBITO (CIRRUS)"""
    check50.run("./debito").stdin("5105105105105100").stdout("CIRRUS\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test4():
    """identifica 5555555555554444 como MASTERCARD DEBITO (CIRRUS)"""
    check50.run("./debito").stdin("5555555555554444").stdout("CIRRUS\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test5():
    """identifica 6500000000000002 como DISCOVERY DEBITO"""
    check50.run("./debito").stdin("6500000000000002").stdout("DISCOVERY DEBITO\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test6():
    """identifica 6011000000000003 como DISCOVERY DEBITO"""
    check50.run("./debito").stdin("6011000000000003").stdout("DISCOVERY DEBITO\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test7():
    """identifica 503396198909013 como MAESTRO"""
    check50.run("./debito").stdin("503396198909013").stdout("MAESTRO\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test8():
    """identifica 6762990000000007 como MAESTRO"""
    check50.run("./debito").stdin("6762990000000007").stdout("MAESTRO\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test9():
    """identifica 1234567890 como INVALID (longitud, checksum, dígitos identificadores inválidos)"""
    check50.run("./debito").stdin("1234567890").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test10():
    """identifica 369421438430814 como INVALID (dígitos identificadores inválidos)"""
    check50.run("./debito").stdin("369421438430814").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test11():
    """identifica 4062901840 como INVALID (longitud inválida)"""
    check50.run("./debito").stdin("4062901840").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test12():
    """identifica 5673598276138003 como INVALID (dígitos identificadores inválidos)"""
    check50.run("./debito").stdin("5673598276138003").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test13():
    """identifica 4111111111111113 como INVALID (checksum inválido)"""
    check50.run("./debito").stdin("4111111111111113").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test14():
    """identifica 4222222222223 como INVALID (checksum inválido)"""
    check50.run("./debito").stdin("4222222222223").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test15():
    """identifica 3400000000000620 como INVALID (dígitos identificadores AMEX, longitud VISA/Mastercard inválidos)"""
    check50.run("./debito").stdin("3400000000000620").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test16():
    """identifica 430000000000000 como INVALID (dígitos identificadores VISA, longitud AMEX inválidos)"""
    check50.run("./debito").stdin("430000000000000").stdout("INVALID\n").stdout(check50.EOF).exit(0)
