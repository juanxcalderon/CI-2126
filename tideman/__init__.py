import check50
import check50.c
import re


@check50.check()
def exists():
    """tideman.c existe"""
    check50.exists("tideman.c")
    check50.include("testing.c")


@check50.check(exists)
def compiles():
    """tideman compila"""
    check50.c.compile("tideman.c", lcs50=True)
    tideman = re.sub("int\s+main", "int distro_main", open("tideman.c").read())
    testing = open("testing.c").read()
    with open("tideman_test.c", "w") as f:
        f.write(tideman)
        f.write("\n")
        f.write(testing)
    check50.c.compile("tideman_test.c", lcs50=True)

@check50.check(compiles)
@check50.hidden("la función de voto no devolvió verdadero")
def vote_returns_true():
    """voto devuelve verdadero cuando se da el nombre del candidato"""
    check50.run("./tideman_test 0 0").stdout("true").exit(0)

@check50.check(compiles)
@check50.hidden("la función de voto no devolvió falso")
def vote_returns_false():
    """voto devuelve falso cuando se da el nombre de un candidato no válido"""
    check50.run("./tideman_test 0 1").stdout("false").exit(0)

@check50.check(compiles)
@check50.hidden("la función de votación no estableció las filas correctamente")
def vote_sets_rank():
    """voto establece correctamente la clasificación para la primera preferencia"""
    check50.run("./tideman_test 0 2").stdout("1").exit(0)

@check50.check(compiles)
@check50.hidden("la función de votación no estableció las filas correctamente")
def vote_sets_all_rank():
    """voto establece correctamente la clasificación para todas las preferencias"""
    check50.run("./tideman_test 0 2").stdout("1 2 0").exit(0)

@check50.check(compiles)
@check50.hidden("la función record_preferences no configuró correctamente las preferencias")
def record_prefs_first():
    """record_preferences establece correctamente las preferencias para el primer votante"""
    check50.run("./tideman_test 0 3").stdout("0 0 0 1 0 1 1 0 0 ").exit(0)

@check50.check(compiles)
@check50.hidden("la función record_preferences no configuró correctamente las preferencias")
def record_prefs_all():
    """record_preferences establece correctamente las preferencias para todos los votantes"""
    check50.run("./tideman_test 0 4").stdout("0 2 2 4 0 5 3 5 0").exit(0)

@check50.check(compiles)
@check50.hidden("La función add_pairs no produjo 3 pares")
def add_pairs1():
    """add_pairs genera un recuento de pares correcto cuando no hay empates"""
    check50.run("./tideman_test 1 5").stdout("3").exit(0)

@check50.check(compiles)
@check50.hidden("La función add_pairs no produjo 2 pares")
def add_pairs2():
    """add_pairs genera un recuento de pares correcto cuando existen vínculos"""
    check50.run("./tideman_test 2 5").stdout("2").exit(0)

@check50.check(compiles)
@check50.hidden("la función add_pairs no produjo pares correctos")
def add_pairs3():
    """add_pairs llena el arreglo de pares con pares ganadores"""
    check50.run("./tideman_test 1 6").stdout("true true true ").exit(0)

@check50.check(compiles)
@check50.hidden("la función add_pairs no produjo pares correctos")
def add_pairs4():
    """add_pairs no llena la matriz de pares con pares perdedores"""
    check50.run("./tideman_test 1 7").stdout("0").exit(0)

@check50.check(compiles)
@check50.hidden("sort_pairs no ordenó correctamente los pares")
def sort_pairs1():
    """sort_pairs ordena pares de candidatos por margen de victoria"""
    check50.run("./tideman_test 3 8").stdout("0 2 0 1 2 1 ").exit(0)

@check50.check(compiles)
@check50.hidden("lock_pairs no bloqueó todos los pares")
def lock_pairs1():
    """lock_pairs bloquea todos los pares cuando no hay ciclos"""
    check50.run("./tideman_test 5 16").stdout("false false false true false true false false false false false false false false false false false false false true false false true false false ").exit(0)

@check50.check(compiles)
@check50.hidden("lock_pairs no bloqueó correctamente todos los pares no cíclicos")
def lock_pairs2():
    """lock_pairs omite el par final si crea un ciclo"""
    check50.run("./tideman_test 6 14").stdout("false true false false false false false false false false true false false false false false false false false false false false false true false false true true false false false false false false false false ").exit(0)

@check50.check(compiles)
@check50.hidden("lock_pairs no bloqueó correctamente todos los pares no cíclicos")
def lock_pairs3():
    """lock_pairs omite el par medio si crea un ciclo"""
    check50.run("./tideman_test 5 15").stdout("false false false false false false false false true false true false false false false false false false false false false true true false false ").exit(0)

@check50.check(compiles)
@check50.hidden("print_winner no imprimió el ganador de la elección")
def print_winner1():
    """print_winner imprime el ganador de la elección cuando un candidato gana a todos los demás"""
    check50.run("./tideman_test 4 12").stdout("^Alice\n?$").exit(0)

@check50.check(compiles)
@check50.hidden("print_winner no imprimió el ganador de la elección")
def print_winner2():
    """print_winner imprime el ganador de la elección cuando algunos pares están empatados"""
    check50.run("./tideman_test 4 13").stdout("^Charlie\n?$").exit(0)
