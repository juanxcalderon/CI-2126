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
def emma():
    """responde al nombre de Emma"""
    check50.run("./hello").stdin("Emma").stdout("¡Hola, Emma!").exit()

@check50.check(compiles)
def rodrigo():
    """responde al nombre de Rodrigo"""
    check50.run("./hello").stdin("Rodrigo").stdout("¡Hola, Rodrigo!").exit()
