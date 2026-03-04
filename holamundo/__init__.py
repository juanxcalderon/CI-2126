import check50
import check50.c

@check50.check()
def exists():
    """hola_mundo.c existe"""
    check50.exists("hola_mundo.c")

@check50.check(exists)
def compiles():
    """hola_mundo.c compila"""
    check50.c.compile("hola_mundo.c", lcs50=True)

@check50.check(compiles)
def emma():
    """responde al nombre de Angela"""
    check50.run("./hola_mundo").stdin("Emma").stdout("¡Hola, Angela!").exit()

@check50.check(compiles)
def rodrigo():
    """responde al nombre de Rodrigo"""
    check50.run("./hola_mundo").stdin("Rodrigo Alvarez").stdout("¡Hola, Rodrigo Alvarez!").exit()

@check50.check(compiles)
def jose():
    """responde al nombre de José Pérez"""
    check50.run("./hola_mundo").stdin("José Pérez").stdout("¡Hola, José Pérez!").exit()
