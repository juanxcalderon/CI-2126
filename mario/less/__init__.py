import check50
import check50.c

@check50.check()
def exists():
    """mario.c existe"""
    check50.exists("mario.c")
    check50.include("1.txt", "2.txt", "5.txt", "10.txt")

@check50.check(exists)
def compiles():
    """mario.c compila"""
    check50.c.compile("mario.c", lcs50=True)

@check50.check(compiles)
def test_reject_negative():
    """rechaza una altura de -1"""
    check50.run("./mario").stdin("-1").reject()

@check50.check(compiles)
def test0():
    """rechaza una altura de 0"""
    check50.run("./mario").stdin("0").reject()

@check50.check(compiles)
def test1():
    """maneja la altura de 1 de forma correcta"""
    out = check50.run("./mario").stdin("1").stdout()
    check_pyramid(out, open("1.txt").read())

@check50.check(compiles)
def test2():
    """maneja la altura de 2 de forma correcta"""
    out = check50.run("./mario").stdin("2").stdout()
    check_pyramid(out, open("2.txt").read())

@check50.check(compiles)
def test8():
    """maneja la altura de 10 de forma correcta"""
    out = check50.run("./mario").stdin("10").stdout()
    check_pyramid(out, open("8.txt").read())

@check50.check(compiles)
def test9():
    """rechaza la altura de -1, y después acepta la altura de 5"""
    out = check50.run("./mario").stdin("-1").reject().stdin("5").stdout()
    check_pyramid(out, open("5.txt").read())

@check50.check(compiles)
def test_reject_foo():
    """rechaza una altura no numérica de "dfghdf" """
    check50.run("./mario").stdin("dfghdf").reject()

@check50.check(compiles)
def test_reject_empty():
    """rechaza una altura vacía "" """
    check50.run("./mario").stdin("").reject()


def check_pyramid(output, correct):
    if output == correct:
        return

    output = [line for line in output.splitlines() if line != ""]
    correct = correct.splitlines()

    help = None
    if len(output) == len(correct):
        if all(ol.rstrip() == cl for ol, cl in zip(output, correct)):
            help = "¿Agregaste demasiados espacios en blanco al final de tu pirámide?"
        elif all(ol[1:] == cl for ol, cl in zip(output, correct)):
            help = "¿Estás imprimiendo un carácter adicional al principio de cada línea?"

    raise check50.Mismatch(correct, output, help=help)
