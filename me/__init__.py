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
    check50.run("./hello").stdin("Emma").stdout("Emma").exit()

@check50.check(compiles)
def inno():
    """responde al nombre de Inno"""
    check50.run("./hello").stdin("Inno").stdout("Inno").exit()

@check50.check(compiles)
def kamryn():
    """responde al nombre de Kamryn"""
    check50.run("./hello").stdin("Kamryn").stdout("Kamryn").exit()
