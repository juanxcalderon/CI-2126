import check50
import check50.c

@check50.check()
def exists():
    """hello.c existe"""
    check50.exists("hello.c")

@check50.check(exists)
def compiles():
    """hello.c compila"""
    check50.c.compile("hello.c", lcs50=True)

@check50.check(compiles)
def world():
    """hello.c imprime \"hola, mundo\""""
    check50.run("./hello").stdout("hola, mundo").exit()
