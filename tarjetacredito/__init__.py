import check50
import check50.c

@check50.check()
def exists():
    """credit.c existe"""
    check50.exists("credit.c")

@check50.check(exists)
def compiles():
    """credit.c compila"""
    check50.c.compile("credit.c", lcs50=True)

@check50.check(compiles)
def test1():
    """identifica 378282246310005 como AMEX"""
    check50.run("./credit").stdin("378282246310005").stdout("AMEX\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test2():
    """identifica 371449635398431 como AMEX"""
    check50.run("./credit").stdin("371449635398431").stdout("AMEX\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test3():
    """identifica 5555555555554444 como MASTERCARD"""
    check50.run("./credit").stdin("5555555555554444").stdout("MASTERCARD\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test4():
    """identifica 5105105105105100 como MASTERCARD"""
    check50.run("./credit").stdin("5105105105105100").stdout("MASTERCARD\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test5():
    """identifica 4111111111111111 como VISA"""
    check50.run("./credit").stdin("4111111111111111").stdout("VISA\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test6():
    """identifica 4012888888881881 como VISA"""
    check50.run("./credit").stdin("4012888888881881").stdout("VISA\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test7():
    """identifica 4222222222222 como VISA"""
    check50.run("./credit").stdin("4222222222222").stdout("VISA\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test8():
    """identifica 1234567890 como INVALID (longitud, checksum, dígitos identificadores inválidos)"""
    check50.run("./credit").stdin("1234567890").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test9():
    """identifica 369421438430814 como INVALID (dígitos identificadores inválidos)"""
    check50.run("./credit").stdin("369421438430814").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test10():
    """identifica 4062901840 como INVALID (longitud inválida)"""
    check50.run("./credit").stdin("4062901840").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test11():
    """identifica 5673598276138003 como INVALID (dígitos identificadores inválidos)"""
    check50.run("./credit").stdin("5673598276138003").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test12():
    """identifica 4111111111111113 como INVALID (checksum inválido)"""
    check50.run("./credit").stdin("4111111111111113").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test13():
    """identifica 4222222222223 como INVALID (checksum inválido)"""
    check50.run("./credit").stdin("4222222222223").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test14():
    """identifica 3400000000000620 como INVALID (dígitos identificadores AMEX, longitud VISA/Mastercard inválidos)"""
    check50.run("./credit").stdin("3400000000000620").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test15():
    """identifica 430000000000000 como INVALID (dígitos identificadores VISA, longitud AMEX inválidos)"""
    check50.run("./credit").stdin("430000000000000").stdout("INVALID\n").stdout(check50.EOF).exit(0)
