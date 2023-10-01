import check50
import check50.c
import re

@check50.check()
def exists():
    """plurality.c existe"""
    check50.exists("plurality.c")
    check50.include("testing.c")


@check50.check(exists)
def compiles():
    """plurality compila"""
    check50.c.compile("plurality.c", lcs50=True)
    plurality = re.sub("int\s+main", "int distro_main", open("plurality.c").read())
    testing = open("testing.c").read()
    with open("plurality_test.c", "w") as f:
        f.write(plurality)
        f.write("\n")
        f.write(testing)
    check50.c.compile("plurality_test.c", lcs50=True)

@check50.check(compiles)
@check50.hidden("la función de voto no devolvió verdadero")
def vote_finds_name_first():
    """voto devuelve verdadero cuando se da el nombre del primer candidato"""
    check50.run("./plurality_test 0 0").stdout("true").exit(0)

@check50.check(compiles)
@check50.hidden("la función de voto no devolvió verdadero")
def vote_finds_name_middle():
    """voto devuelve verdadero cuando se da el nombre del candidato del medio"""
    check50.run("./plurality_test 0 1").stdout("true").exit(0)

@check50.check(compiles)
@check50.hidden("la función de voto no devolvió verdadero")
def vote_finds_name_last():
    """voto devuelve verdadero cuando se da el nombre del último candidato"""
    check50.run("./plurality_test 0 2").stdout("true").exit(0)

@check50.check(compiles)
@check50.hidden("La función de voto no devolvió falso")
def vote_returns_false():
    """voto devuelve falso cuando se da el nombre de un candidato no válido"""
    check50.run("./plurality_test 0 3").stdout("false").exit(0)

@check50.check(compiles)
@check50.hidden("la función de votación no actualizó correctamente los totales de votos")
def first_vote_totals_correct():
    """la votación produce recuentos correctos cuando todos los votos son cero"""
    check50.run("./plurality_test 0 4").stdout("1 0 0").exit(0)

@check50.check(compiles)
@check50.hidden("la función de votación no actualizó correctamente los totales de votos")
def subsequent_vote_totals_correct():
    """la votación produce recuentos correctos después de que algunos ya han votado"""
    check50.run("./plurality_test 0 5").stdout("2 8 0").exit(0)

@check50.check(compiles)
@check50.hidden("La función de votación modificó los totales de votos incorrectamente.")
def invalid_vote_votes_unchanged():
    """la votación deja el recuento de votos sin cambios cuando se vota por un candidato inválido"""
    check50.run("./plurality_test 0 6").stdout("2 8 0").exit(0)

@check50.check(compiles)
@check50.hidden("la función print_winner no imprimió el ganador de la elección")
def print_winner0():
    """print_winner identifica a Alice como la ganadora de la elección"""
    check50.run("./plurality_test 0 7").stdout("^Alice\n?$").exit(0)

@check50.check(compiles)
@check50.hidden("la función print_winner no imprimió el ganador de la elección")
def print_winner1():
    """print_winner identifica a Bob como el ganador de la elección"""
    check50.run("./plurality_test 0 8").stdout("^Bob\n?$").exit(0)

@check50.check(compiles)
@check50.hidden("la función print_winner no imprimió el ganador de la elección")
def print_winner2():
    """print_winner identifica a Charlie como el ganador de la elección"""
    check50.run("./plurality_test 0 9").stdout("^Charlie\n?$").exit(0)

@check50.check(compiles)
@check50.hidden("la función print_winner no imprimió a los dos ganadores de la elección")
def print_winner3():
    """print_winner imprime múltiples ganadores en caso de empate"""
    result = check50.run("./plurality_test 0 10").stdout()
    if set(result.split("\n")) - {""} != {"Alice", "Bob"}:
        raise check50.Mismatch("Alice\nBob\nCharlie\n", result)

@check50.check(compiles)
@check50.hidden("la función print_winner no imprimió a los tres ganadores de la elección")
def print_winner4():
    """print_winner imprime todos los nombres cuando todos los candidatos están empatados"""
    result = check50.run("./plurality_test 0 11").stdout()
    if set(result.split("\n")) - {""} != {"Alice", "Bob", "Charlie"}:
        raise check50.Mismatch("Alice\nBob\nCharlie\n", result)
