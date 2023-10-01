import check50
from re import search
from re import findall

@check50.check()
def exists():
    """answers.txt existe"""
    check50.exists("answers.txt")

@check50.check(exists)
def answers():
    """responde todas las preguntas"""
    content = open("answers.txt", "r").read()
    if "TODO" in content:
        raise check50.Failure("No todas las preguntas son respondidas.")

@check50.check(exists)
def sorts():
    """identifica correctamente cada ordenación"""

    check50.log("comprobando que los tipos están clasificados correctamente...")

    expected = ["sort1 uses:\s*[Bb][Uu][Bb][Bb][Ll][Ee]", "sort2 uses:\s*[Mm][Ee][Rr][Gg][Ee]", "sort3 uses:\s*[Ss][Ee][Ll][Ee][Cc][Tt][Ii][Oo][Nn]"]
    actual = open("answers.txt", "r").read()

    for e in expected:
        if not search(e, actual):
            raise check50.Failure("Asignación incorrecta de ordenamientos.")

