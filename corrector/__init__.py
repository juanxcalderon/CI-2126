import check50
import check50.c
import os


@check50.check()
def exists():
    """diccionario.c existe"""
    check50.exists("diccionario.c")


@check50.check(exists)
def compiles():
    """corrector compila"""
    check50.include("corrector.c", "Makefile")
    if not os.path.exists("diccionario.h"):
        check50.include("diccionario.h")
    check50.run("make").exit(0)


@check50.check(compiles)
def basic():
    """maneja correctamente las palabras más básicas"""
    check50.include("basic")
    check50.run("./corrector basic/dict basic/text").stdout(open("basic/out")).exit(0)


@check50.check(compiles)
def min_length():
    """maneja palabras de longitud mínima (1 carácter)"""
    check50.include("min_length")
    check50.run("./corrector min_length/dict min_length/text").stdout(open("min_length/out")).exit(0)


@check50.check(compiles)
def max_length():
    """maneja palabras de longitud máxima (45 caracteres)"""
    check50.include("max_length")
    check50.run("./corrector max_length/dict max_length/text").stdout(open("max_length/out")).exit(0)


@check50.check(compiles)
def apostrophe():
    """maneja correctamente las palabras con apóstrofes"""
    check50.include("apostrophe")
    # Diccionario sin apóstrofe, texto con apóstrofe → "foo's" debe ser error
    check50.run("./corrector apostrophe/without/dict apostrophe/with/text").stdout(
        open("apostrophe/outs/without-with")
    ).exit(0)
    # Diccionario con apóstrofe, texto sin apóstrofe → las 8 variantes de "foo" deben ser error
    check50.run("./corrector apostrophe/with/dict apostrophe/without/text").stdout(
        open("apostrophe/outs/with-without")
    ).exit(0)
    # Diccionario con apóstrofe, texto con apóstrofe → ningún error
    check50.run("./corrector apostrophe/with/dict apostrophe/with/text").stdout(
        open("apostrophe/outs/with-with")
    ).exit(0)


@check50.check(compiles)
def case():
    """la revisión ortográfica no distingue entre mayúsculas y minúsculas"""
    check50.include("case")
    check50.run("./corrector case/dict case/text").stdout(open("case/out")).exit(0)


@check50.check(compiles)
def substring():
    """maneja subcadenas correctamente (cat ≠ cats, cat ≠ caterpillar)"""
    check50.include("substring")
    check50.run("./corrector substring/dict substring/text").stdout(open("substring/out")).exit(0)


@check50.check(substring)
def memory():
    """el programa no tiene fugas ni errores de memoria"""
    check50.c.valgrind("./corrector substring/dict substring/text").stdout(
        open("substring/out"), timeout=10
    ).exit(0)
