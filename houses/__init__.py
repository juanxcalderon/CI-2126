from cs50 import SQL

import check50
import re

@check50.check()
def exists():
    """import.py y roster.py existen"""
    check50.exists("import.py", "roster.py")
    check50.include("students.db", "students.csv")

@check50.check(exists)
def import1():
    """import.py importa correctamente Harry Potter"""
    check50.run("python3 import.py students.csv").exit(timeout=10)
    db = SQL("sqlite:///students.db")
    rows = db.execute("SELECT first, middle, last, house, birth FROM students WHERE first = 'Harry'")
    expected = [{"first": "Harry", "middle": "James", "last": "Potter", "house": "Gryffindor", "birth": 1980}]
    if rows != expected:
        raise check50.Mismatch(str(expected), str(rows))

@check50.check(exists)
def import2():
    """import.py importa correctamente Luna Lovegood"""
    check50.run("python3 import.py students.csv").exit(timeout=10)
    db = SQL("sqlite:///students.db")
    rows = db.execute("SELECT first, middle, last, house, birth FROM students WHERE first = 'Luna'")
    expected = [{"first": "Luna", "middle": None, "last": "Lovegood", "house": "Ravenclaw", "birth": 1981}]
    if rows != expected:
        raise check50.Mismatch(str(expected), str(rows))

@check50.check(exists)
def import_count():
    """import.py importa el número correcto de filas"""
    check50.run("python3 import.py students.csv").exit(timeout=10)
    db = SQL("sqlite:///students.db")
    actual = db.execute("SELECT COUNT(*) as count FROM students")[0]["count"]
    expected = 40
    if actual != expected:
        raise check50.Mismatch(str(expected), str(actual))

@check50.check(import_count)
def roster_hufflepuff():
    """roster.py genera correctamente la nómina de Hufflepuff"""
    check50.include("hufflepuff.txt", "hufflepuff_re.txt")
    actual = check50.run("python3 roster.py Hufflepuff").stdout(timeout=10)
    if not re.search(open("hufflepuff_re.txt").read(), actual):
        raise check50.Mismatch(open("hufflepuff.txt").read(), actual)

@check50.check(import_count)
def roster_gryffindor():
    """roster.py genera correctamente la nómina de Gryffindor"""
    check50.include("gryffindor.txt", "gryffindor_re.txt")
    actual = check50.run("python3 roster.py Gryffindor").stdout(timeout=10)
    if not re.search(open("gryffindor_re.txt").read(), actual):
        raise check50.Mismatch(open("gryffindor.txt").read(), actual)
