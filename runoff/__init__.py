import check50
import check50.c
import re


@check50.check()
def exists():
    """runoff.c existe"""
    check50.exists("runoff.c")
    check50.include("testing.c")


@check50.check(exists)
def compiles():
    """runoff compila"""
    check50.c.compile("runoff.c", lcs50=True)
    runoff = re.sub("int\s+main", "int distro_main", open("runoff.c").read())
    testing = open("testing.c").read()
    with open("runoff_test.c", "w") as f:
        f.write(runoff)
        f.write("\n")
        f.write(testing)
    check50.c.compile("runoff_test.c", lcs50=True)

@check50.check(compiles)
@check50.hidden("la función de voto no devolvió verdadero")
def vote_returns_true():
    """voto devuelve verdadero cuando se da el nombre del candidato"""
    check50.run("./runoff_test 0 0").stdout("true").exit(0)

@check50.check(compiles)
@check50.hidden("la función de voto no devolvió falso")
def vote_returns_false():
    """voto devuelve falso cuando se da el nombre de un candidato no válido"""
    check50.run("./runoff_test 0 1").stdout("false").exit(0)

@check50.check(compiles)
@check50.hidden("la función de voto no estableció correctamente las preferencias")
def vote_sets_preference1():
    """voto establece correctamente la primera preferencia para el primer votante"""
    check50.run("./runoff_test 0 2").stdout("2").exit(0)

@check50.check(compiles)
@check50.hidden("la función de voto no estableció correctamente las preferencias")
def vote_sets_preference2():
    """voto establece correctamente la tercera preferencia por el segundo votante"""
    check50.run("./runoff_test 0 3").stdout("0").exit(0)

@check50.check(compiles)
@check50.hidden("la función de voto no estableció correctamente las preferencias")
def vote_sets_all_preferences():
    """voto establece correctamente todas las preferencias para el votante"""
    check50.run("./runoff_test 0 4").stdout("1 0 2").exit(0)

@check50.check(compiles)
@check50.hidden("la función de tabulación no produjo totales de votos correctos")
def tabulate1():
    """tabular cuenta los votos cuando todos los candidatos permanecen en la elección"""
    check50.run("./runoff_test 1 5").stdout("3 3 1 0 ").exit(0)

@check50.check(compiles)
@check50.hidden("la función de tabulación no produjo totales de votos correctos")
def tabulate2():
    """tabular cuenta los votos cuando un candidato es eliminado"""
    check50.run("./runoff_test 1 6").stdout("3 3 1 0 ").exit(0)

@check50.check(compiles)
@check50.hidden("la función de tabulación no produjo totales de votos correctos")
def tabulate3():
    """tabular cuenta votos cuando se eliminan varios candidatos"""
    check50.run("./runoff_test 1 7").stdout("3 4 0 0 ").exit(0)

@check50.check(compiles)
@check50.hidden("la función de tabulación no produjo totales de votos correctos")
def tabulate4():
    """tabular maneja múltiples rondas de preferencias"""
    check50.run("./runoff_test 1 22").stdout("3 4 0 0 ").exit(0)

@check50.check(compiles)
@check50.hidden("print_winner no imprimió el ganador de la elección")
def print_winner1():
    """print_winner imprime el nombre cuando alguien tiene mayoría"""
    check50.run("./runoff_test 2 8").stdout("Bob\n").exit(0)

@check50.check(compiles)
@check50.hidden("print_winner no imprimió el ganador y luego devolvió verdadero")
def print_winner2():
    """print_winner devuelve verdadero cuando alguien tiene la mayoría"""
    check50.run("./runoff_test 2 9").stdout("Bob\ntrue").exit(0)

@check50.check(compiles)
@check50.hidden("print_winner no devolvió falso")
def print_winner3():
    """print_winner devuelve falso cuando nadie tiene mayoría"""
    check50.run("./runoff_test 2 10").stdout("false").exit(0)

@check50.check(compiles)
@check50.hidden("print_winner no devolvió falso")
def print_winner4():
    """print_winner devuelve falso cuando el líder tiene exactamente el 50% de los votos"""
    check50.run("./runoff_test 2 11").stdout("false").exit(0)

@check50.check(compiles)
@check50.hidden("find_min no identificó el mínimo correcto")
def find_min1():
    """find_min devuelve el número mínimo de votos para el candidato"""
    check50.run("./runoff_test 2 12").stdout("1").exit(0)

@check50.check(compiles)
@check50.hidden("find_min no identificó el mínimo correcto")
def find_min2():
    """find_min devuelve mínimo cuando todos los candidatos están empatados"""
    check50.run("./runoff_test 2 13").stdout("7").exit(0)

@check50.check(compiles)
@check50.hidden("find_min no identificó el mínimo correcto")
def find_min3():
    """find_min ignora a los candidatos eliminados"""
    check50.run("./runoff_test 2 14").stdout("4").exit(0)

@check50.check(compiles)
@check50.hidden("is_tie no devolvió verdadero")
def is_tie1():
    """is_tie devuelve verdadero cuando la elección está empatada"""
    check50.run("./runoff_test 2 15").stdout("true").exit(0)

@check50.check(compiles)
@check50.hidden("is_tie no devolvió falso")
def is_tie2():
    """Is_tie devuelve falso cuando la elección no está empatada"""
    check50.run("./runoff_test 2 16").stdout("false").exit(0)

@check50.check(compiles)
@check50.hidden("is_tie no devolvió falso")
def is_tie3():
    """is_tie devuelve falso cuando solo algunos de los candidatos están empatados"""
    check50.run("./runoff_test 2 17").stdout("false").exit(0)

@check50.check(compiles)
@check50.hidden("is_tie no devolvió verdadero")
def is_tie4():
    """is_tie detecta empate después de que algunos candidatos hayan sido eliminados"""
    check50.run("./runoff_test 2 18").stdout("true").exit(0)

@check50.check(compiles)
@check50.hidden("eliminate no eliminó a los candidatos correctos")
def eliminate1():
    """eliminate elimina candidato en último lugar"""
    check50.run("./runoff_test 2 19").stdout("false false false true ").exit(0)

@check50.check(compiles)
@check50.hidden("eliminate no eliminó a los candidatos correctos")
def eliminate2():
    """eliminate elimina múltiples candidatos en empate para el último"""
    check50.run("./runoff_test 2 20").stdout("true false true false ").exit(0)

@check50.check(compiles)
@check50.hidden("eliminate no eliminó a los candidatos correctos")
def eliminate3():
    """eliminate elimina candidatos después de que algunos ya hayan sido eliminados"""
    check50.run("./runoff_test 2 21").stdout("true false true false ").exit(0)
