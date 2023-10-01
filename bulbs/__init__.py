import check50
import check50.c


@check50.check()
def exists():
    """bulbs.c existe"""
    check50.exists("bulbs.c")


@check50.check(exists)
def compiles():
    """bulbs.c compila"""
    check50.c.compile("bulbs.c", lcs50=True)


@check50.check(compiles)
def bulbs_empty():
    """bulbifica correctamente un mensaje vacío"""
    check50.run("./bulbs").stdin("").stdout("").exit(0)
    

@check50.check(compiles)
def bulbs_single_letter():
    """bulbifica \"I\" correctamente"""
    check50.run("./bulbs").stdin("I").stdout("⚫🟡⚫⚫🟡⚫⚫🟡\n").exit(0)
    

@check50.check(compiles)
def bulbs_multiple_letters():
    """bulbifica \"xyz\" correctamente"""
    check50.run("./bulbs").stdin("xyz").stdout("⚫🟡🟡🟡🟡⚫⚫⚫\n⚫🟡🟡🟡🟡⚫⚫🟡\n⚫🟡🟡🟡🟡⚫🟡⚫\n").exit(0)


@check50.check(compiles)
def bulbs_non_alpha():
    """bulbifica \"?\" correctamente"""
    check50.run("./bulbs").stdin("?").stdout("⚫⚫🟡🟡🟡🟡🟡🟡\n").exit(0)


@check50.check(compiles)
def bulbs_message():
    """bulbifica \"Hi!\" correctamente"""
    check50.run("./bulbs").stdin("Hi!").stdout("⚫🟡⚫⚫🟡⚫⚫⚫\n⚫🟡🟡⚫🟡⚫⚫🟡\n⚫⚫🟡⚫⚫⚫⚫🟡\n").exit(0)
    

@check50.check(compiles)
def bulbs_mixed_case_alpha():
    """bulbifica \"aBcDeFgHiJkLmNoPqRsTuVwXyZ\" correctamente"""
    check50.run("./bulbs").stdin("aBcDeFgHiJkLmNoPqRsTuVwXyZ").stdout("⚫🟡🟡⚫⚫⚫⚫🟡\n⚫🟡⚫⚫⚫⚫🟡⚫\n⚫🟡🟡⚫⚫⚫🟡🟡\n⚫🟡⚫⚫⚫🟡⚫⚫\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫🟡⚫⚫⚫🟡🟡⚫\n⚫🟡🟡⚫⚫🟡🟡🟡\n⚫🟡⚫⚫🟡⚫⚫⚫\n⚫🟡🟡⚫🟡⚫⚫🟡\n⚫🟡⚫⚫🟡⚫🟡⚫\n⚫🟡🟡⚫🟡⚫🟡🟡\n⚫🟡⚫⚫🟡🟡⚫⚫\n⚫🟡🟡⚫🟡🟡⚫🟡\n⚫🟡⚫⚫🟡🟡🟡⚫\n⚫🟡🟡⚫🟡🟡🟡🟡\n⚫🟡⚫🟡⚫⚫⚫⚫\n⚫🟡🟡🟡⚫⚫⚫🟡\n⚫🟡⚫🟡⚫⚫🟡⚫\n⚫🟡🟡🟡⚫⚫🟡🟡\n⚫🟡⚫🟡⚫🟡⚫⚫\n⚫🟡🟡🟡⚫🟡⚫🟡\n⚫🟡⚫🟡⚫🟡🟡⚫\n⚫🟡🟡🟡⚫🟡🟡🟡\n⚫🟡⚫🟡🟡⚫⚫⚫\n⚫🟡🟡🟡🟡⚫⚫🟡\n⚫🟡⚫🟡🟡⚫🟡⚫\n").exit(0)


@check50.check(compiles)
def bulbs_spaces():
    """bulbifica \" CS50 :) \" correctamente"""
    check50.run("./bulbs").stdin(" CS50 :) ").stdout("⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡⚫⚫⚫⚫🟡🟡\n⚫🟡⚫🟡⚫⚫🟡🟡\n⚫⚫🟡🟡⚫🟡⚫🟡\n⚫⚫🟡🟡⚫⚫⚫⚫\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫⚫🟡🟡🟡⚫🟡⚫\n⚫⚫🟡⚫🟡⚫⚫🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n").exit(0)


@check50.check(compiles)
def bulbs_finale():
    """Bulbifica correctamente la primera frase de The Great Gatsby"""
    check50.run("./bulbs").stdin("In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.").stdout("⚫🟡⚫⚫🟡⚫⚫🟡\n⚫🟡🟡⚫🟡🟡🟡⚫\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫🟡🟡⚫🟡\n⚫🟡🟡🟡🟡⚫⚫🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡🟡🟡⚫⚫🟡\n⚫🟡🟡⚫🟡🟡🟡🟡\n⚫🟡🟡🟡⚫🟡⚫🟡\n⚫🟡🟡⚫🟡🟡🟡⚫\n⚫🟡🟡⚫⚫🟡🟡🟡\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫🟡🟡🟡⚫⚫🟡⚫\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫⚫⚫⚫🟡\n⚫🟡🟡⚫🟡🟡🟡⚫\n⚫🟡🟡⚫⚫🟡⚫⚫\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫🟡🟡⚫🟡\n⚫🟡🟡⚫🟡🟡🟡🟡\n⚫🟡🟡🟡⚫⚫🟡⚫\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡🟡⚫🟡🟡⚫\n⚫🟡🟡🟡⚫🟡⚫🟡\n⚫🟡🟡⚫🟡🟡⚫⚫\n⚫🟡🟡⚫🟡🟡🟡⚫\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫🟡🟡🟡⚫⚫🟡⚫\n⚫🟡🟡⚫⚫⚫⚫🟡\n⚫🟡🟡⚫⚫⚫🟡⚫\n⚫🟡🟡⚫🟡🟡⚫⚫\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡🟡🟡⚫⚫🟡\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫🟡🟡⚫⚫⚫⚫🟡\n⚫🟡🟡🟡⚫⚫🟡⚫\n⚫🟡🟡🟡⚫⚫🟡🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫🟡🟡⚫🟡\n⚫🟡🟡🟡🟡⚫⚫🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫⚫🟡🟡⚫\n⚫🟡🟡⚫⚫⚫⚫🟡\n⚫🟡🟡🟡⚫🟡⚫⚫\n⚫🟡🟡⚫🟡⚫⚫⚫\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫🟡🟡🟡⚫⚫🟡⚫\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫⚫🟡🟡🟡\n⚫🟡🟡⚫⚫⚫⚫🟡\n⚫🟡🟡🟡⚫🟡🟡⚫\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫🟡🟡⚫🟡\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡🟡⚫⚫🟡🟡\n⚫🟡🟡⚫🟡🟡🟡🟡\n⚫🟡🟡⚫🟡🟡⚫🟡\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫⚫⚫⚫🟡\n⚫🟡🟡⚫⚫🟡⚫⚫\n⚫🟡🟡🟡⚫🟡🟡⚫\n⚫🟡🟡⚫🟡⚫⚫🟡\n⚫🟡🟡⚫⚫⚫🟡🟡\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡🟡⚫🟡⚫⚫\n⚫🟡🟡⚫🟡⚫⚫⚫\n⚫🟡🟡⚫⚫⚫⚫🟡\n⚫🟡🟡🟡⚫🟡⚫⚫\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡⚫⚫🟡⚫⚫🟡\n⚫⚫🟡⚫⚫🟡🟡🟡\n⚫🟡🟡🟡⚫🟡🟡⚫\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫⚫⚫🟡⚫\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫🟡🟡⚫🟡🟡🟡⚫\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡🟡⚫🟡⚫⚫\n⚫🟡🟡🟡⚫🟡⚫🟡\n⚫🟡🟡🟡⚫⚫🟡⚫\n⚫🟡🟡⚫🟡🟡🟡⚫\n⚫🟡🟡⚫🟡⚫⚫🟡\n⚫🟡🟡⚫🟡🟡🟡⚫\n⚫🟡🟡⚫⚫🟡🟡🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫🟡🟡🟡🟡\n⚫🟡🟡🟡⚫🟡🟡⚫\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫🟡🟡🟡⚫⚫🟡⚫\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫🟡⚫⚫🟡\n⚫🟡🟡⚫🟡🟡🟡⚫\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫🟡🟡⚫🟡\n⚫🟡🟡🟡🟡⚫⚫🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫🟡🟡⚫🟡\n⚫🟡🟡⚫🟡⚫⚫🟡\n⚫🟡🟡⚫🟡🟡🟡⚫\n⚫🟡🟡⚫⚫🟡⚫⚫\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫🟡🟡🟡⚫🟡🟡⚫\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫🟡🟡🟡⚫⚫🟡⚫\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡🟡⚫⚫🟡🟡\n⚫🟡🟡⚫🟡⚫⚫🟡\n⚫🟡🟡⚫🟡🟡🟡⚫\n⚫🟡🟡⚫⚫⚫🟡🟡\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫⚫🟡⚫🟡🟡🟡⚫\n").exit(0)
