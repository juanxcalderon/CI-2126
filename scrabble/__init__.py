import check50
import check50.c

@check50.check()
def exists():
    """scrabble.c existe"""
    check50.exists("scrabble.c")

@check50.check(exists)
def compiles():
    """scrabble.c compila"""
    check50.c.compile("scrabble.c", lcs50=True)

@check50.check(compiles)
def tie_letter_case():
    """maneja correctamente las mayúsculas y minúsculas"""
    check50.run("./scrabble").stdin("LETTERCASE").stdin("lettercase").stdout("[Tt]ie!?", "Tie!").exit(0)

@check50.check(compiles)
def tie_punctuation():
    """maneja la puntuación correctamente"""
    check50.run("./scrabble").stdin("Punctuation!?!?").stdin("punctuation").stdout("[Tt]ie!?", "Tie!").exit(0)

@check50.check(compiles)
def test1():
    """identifica correctamente 'Question?' y 'Question!' como un empate"""
    check50.run("./scrabble").stdin("Question?").stdin("Question!").stdout("[Tt]ie!?", "Tie!").exit(0)

@check50.check(compiles)
def test2():
    """identifica correctamente 'drawing' e 'illustration' como un empate"""
    check50.run("./scrabble").stdin("drawing").stdin("illustration").stdout("[Tt]ie!?", "Tie!").exit(0)

@check50.check(compiles)
def test3():
    """identifica correctamente 'hai!' como ganador sobre 'Oh,'"""
    check50.run("./scrabble").stdin("Oh,").stdin("hai!").stdout("[Pp]layer 2 [Ww]ins!?", "Player 2 wins!").exit(0)

@check50.check(compiles)
def test4():
    """identifica correctamente 'COMPUTER' como ganador sobre 'science'"""
    check50.run("./scrabble").stdin("COMPUTER").stdin("science").stdout("[Pp]layer 1 [Ww]ins!?", "Player 1 wins!").exit(0)

@check50.check(compiles)
def test5():
    """identifica correctamente 'Scrabble' como ganador sobre 'wiNNeR'"""
    check50.run("./scrabble").stdin("Scrabble").stdin("wiNNeR").stdout("[Pp]layer 1 [Ww]ins!?", "Player 1 wins!").exit(0)

@check50.check(compiles)
def test6():
    """identifica correctamente 'pig' como ganador sobre 'dog'"""
    check50.run("./scrabble").stdin("pig").stdin("dog").stdout("[Pp]layer 1 [Ww]ins!?", "Player 1 wins!").exit(0)

@check50.check(compiles)
def complex_case():
    """identifica correctamente 'Skating!' como ganador sobre 'figure?'"""
    check50.run("./scrabble").stdin("figure?").stdin("Skating!").stdout("[Pp]layer 2 [Ww]ins!?", "Player 2 wins!").exit(0)

