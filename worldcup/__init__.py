import os
import re
import check50
import check50.py

BRACKET2 = [
    {"team": "Uruguay", "rating": 976},
    {"team": "Portugal", "rating": 1306},
]
BRACKET4 = [
    {"team": "Uruguay", "rating": 976},
    {"team": "Portugal", "rating": 1306},
    {"team": "France", "rating": 1166},
    {"team": "Argentina", "rating": 1254},
]
BRACKET8 = [
    {"team": "Uruguay", "rating": 976},
    {"team": "Portugal", "rating": 1306},
    {"team": "France", "rating": 1166},
    {"team": "Argentina", "rating": 1254},
    {"team": "Brazil", "rating": 1384},
    {"team": "Mexico", "rating": 1008},
    {"team": "Belgium", "rating": 1346},
    {"team": "Japan", "rating": 528},
]
BRACKET16 = [
    {"team": "Uruguay", "rating": 976},
    {"team": "Portugal", "rating": 1306},
    {"team": "France", "rating": 1166},
    {"team": "Argentina", "rating": 1254},
    {"team": "Brazil", "rating": 1384},
    {"team": "Mexico", "rating": 1008},
    {"team": "Belgium", "rating": 1346},
    {"team": "Japan", "rating": 528},
    {"team": "Spain", "rating": 1162},
    {"team": "Russia", "rating": 493},
    {"team": "Croatia", "rating": 975},
    {"team": "Denmark", "rating": 1054},
    {"team": "Sweden", "rating": 889},
    {"team": "Switzerland", "rating": 1179},
    {"team": "Colombia", "rating": 989},
    {"team": "England", "rating": 1040},
]
QUESTIONS = [
    "¿Qué predicciones, si las hubo, resultaron incorrectas a medida que aumentaste el número de simulaciones?",
    'Supongamos que le cobran una tarifa por cada segundo de tiempo de cálculo que utiliza su programa.\n¿Después de cuántas simulaciones consideraría que las predicciones son "suficientemente buenas"?',
]
SIMULATION_RUNS = [
    "10",
    "100",
    "1000",
    "10000",
    "100000",
    "1000000",
]


@check50.check()
def exists():
    """tournament.py existe"""
    check50.exists("tournament.py", "answers.txt")
    check50.include("2018m.csv", "2019w.csv")


@check50.check(exists)
def imports():
    """tournament.py importa"""
    check50.py.import_("tournament.py")


@check50.check(imports)
def sim_tournament_2():
    """simulate_tournament maneja un grupo de tamaño 2"""
    check_tournament(BRACKET2)


@check50.check(imports)
def sim_tournament_4():
    """simulate_tournament maneja un grupo de tamaño 4"""
    check_tournament(BRACKET4)


@check50.check(imports)
def sim_tournament_8():
    """simulate_tournament maneja un grupo de tamaño 8"""
    check_tournament(BRACKET8)


@check50.check(imports)
def sim_tournament_16():
    """simulate_tournament maneja un grupo de tamaño 16"""
    check_tournament(BRACKET16)


@check50.check(imports)
def counts():
    """realiza un seguimiento correcto de partidos ganados"""
    actual = check50.run("python3 tournament.py 2018m.csv").stdout()
    percents = re.findall("[0-9]*\.[0-9]", actual)
    percents = [float(x) for x in percents]
    if sum(percents) < 99 or sum(percents) > 101:
        raise check50.Failure("falla en hacer seguimiento de partidos ganados")


@check50.check(imports)
def correct_teams1():
    """reporta correctamente la información del equipo para la Copa Mundial Masculina"""
    actual = check50.run("python3 tournament.py 2018m.csv").stdout()
    expected = ["Belgium", "Brazil", "Portugal", "Spain"]
    not_expected = ["Germany"]
    for team in expected:
        if team not in actual:
            raise check50.Failure(f"no encontró el equipo de {team}")
    for team in not_expected:
        if team in actual:
            raise check50.Failure(f"equipo {team} encontrado incorrectamente")


@check50.check(imports)
def correct_teams2():
    """reporta correctamente la información del equipo para la Copa Mundial Femenina"""
    actual = check50.run("python3 tournament.py 2019w.csv").stdout()
    expected = ["Germany", "United States", "England"]
    not_expected = ["Belgium"]
    for team in expected:
        if team not in actual:
            raise check50.Failure(f"no encontró el equipo de {team}")
    for team in not_expected:
        if team in actual:
            raise check50.Failure(f"equipo {team} encontrado incorrectamente")

    percents = re.findall("[0-9]*\.[0-9]", actual)
    percents = [float(x) for x in percents]
    if sum(percents) < 99 or sum(percents) > 101:
        raise check50.Failure("falla en hacer seguimiento de partidos ganados")


@check50.check(imports)
def check_answers():
    """answers.txt está completo"""
    with open("answers.txt") as f:
        contents = f.read()

        # Check timings
        for runs in SIMULATION_RUNS:
            match = re.search(
                rf"(?i){re.escape(runs)} simulations:\s*(\d+m\d+\.\d\d\ds)(?<!0m0\.000s)",
                contents,
            )
            if not match:
                raise check50.Failure(
                    "answers.txt no incluye tiempos para cada número de ejecuciones de simulación",
                    help="¿Pusiste todas tus respuestas en formato 0m0.000s?",
                )

        # Check free response
        num_questions = len(QUESTIONS)
        for i, question in enumerate(QUESTIONS):

            # Search for question, with at least 3 words afterwards
            if i + 1 < num_questions:

                # Regex includes question being asked, response, and following question
                regex = (
                    rf"(?i){re.escape(question)}"
                    + r":\s*(\S+\s+){3,}"
                    + rf"{re.escape(QUESTIONS[i + 1])}"
                )
            else:

                # Last regex includes question being asked and response
                regex = rf"(?i){re.escape(question)}" + r":\s*(\S+\s+){3,}"

            match = re.search(regex, contents)
            if not match:
                raise check50.Failure(
                    "answers.txt no incluye respuestas a preguntas de respuesta libre",
                    help="¿Escribiste una respuesta suficiente a cada pregunta?",
                )


# Helpers


def check_round(*args):
    tournament = check50.py.import_("tournament.py")
    actual = tournament.simulate_round(args[0])

    for i in range(len(actual)):
        expected = [args[0][2 * i], args[0][2 * i + 1]]
        if not (actual[i] in expected):
            raise check50.Failure(
                "simulate_round no logra determinar los ganadores en una ronda"
            )


def check_tournament(*args):
    tournament = check50.py.import_("tournament.py")
    actual = tournament.simulate_tournament(args[0])
    teams = [x["team"] for x in args[0]]

    if not actual in teams:
        raise check50.Failure(
            "simulate_tournament no devuelve el nombre de 1 equipo ganador"
        )
