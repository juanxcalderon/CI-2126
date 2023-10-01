import re

import check50


@check50.check()
def exists():
    """log.sql y answers.txt existen"""
    check50.exists("log.sql", "answers.txt")

@check50.check(exists)
def log_file():
    """log file contiene consultas SELECT"""

    log = open("log.sql").read().lower()
    if "select" not in log:
        raise check50.Failure(f"faltan consultas SELECT en log.sql")

@check50.check(exists)
def solved():
    """misterio resuelto"""

    answers = open("answers.txt").read().lower()

    thief = "6272756365"
    city = "6e657720796f726b"
    accomplice = "726f62696e"

    for q in ["ladrón es", "escapó a", "cómplice es"]:
        if answers.count(q) > 1:
            raise check50.Failure("formato de answers.txt no válido")

    identify_thief = re.search(f"ladrón\s*es\s*:?\s*{bytes.fromhex(thief).decode('utf-8')}", answers)
    identify_city = re.search(f"escapó\s*a\s*:?\s*{bytes.fromhex(city).decode('utf-8')}", answers)
    identify_accomplice = re.search(f"cómplice\s*es\s*:?\s*{bytes.fromhex(accomplice).decode('utf-8')}", answers)
    if not identify_thief or not identify_city or not identify_accomplice:
        raise check50.Failure(f"answers.txt no resuelve correctamente el misterio")
