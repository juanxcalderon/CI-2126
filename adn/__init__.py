import check50

@check50.check()
def exists():
    """adn.py existe"""
    check50.exists("adn.py")
    check50.include("sequences", "databases")

@check50.check(exists)
def test1():
    """identifica correctamente sequences/1.txt"""
    check50.run("python3 adn.py databases/small.csv sequences/1.txt").stdout("^Bob", "Bob\n", timeout=5).exit()

@check50.check(exists)
def test2():
    """identifica correctamente sequences/2.txt"""
    check50.run("python3 adn.py databases/small.csv sequences/2.txt").stdout("^[Nn]o [Mm]atch\.?\n", "No match\n", timeout=5).exit()

@check50.check(exists)
def test3():
    """identifica correctamente sequences/3.txt"""
    check50.run("python3 adn.py databases/small.csv sequences/3.txt").stdout("^[Nn]o [Mm]atch\.?\n", "No match\n", timeout=5).exit()

@check50.check(exists)
def test4():
    """identifica correctamente sequences/4.txt"""
    check50.run("python3 adn.py databases/small.csv sequences/4.txt").stdout("^Alice", "Alice\n", timeout=5).exit()

@check50.check(exists)
def test5():
    """identifica correctamente sequences/5.txt"""
    check50.run("python3 adn.py databases/large.csv sequences/5.txt").stdout("^Lavender", "Lavender\n", timeout=5).exit()

@check50.check(exists)
def test6():
    """identifica correctamente sequences/6.txt"""
    check50.run("python3 adn.py databases/large.csv sequences/6.txt").stdout("^Luna", "Luna\n", timeout=5).exit()

@check50.check(exists)
def test7():
    """identifica correctamente sequences/7.txt"""
    check50.run("python3 adn.py databases/large.csv sequences/7.txt").stdout("^Ron", "Ron\n", timeout=5).exit()

@check50.check(exists)
def test8():
    """identifica correctamente sequences/8.txt"""
    check50.run("python3 adn.py databases/large.csv sequences/8.txt").stdout("^Ginny", "Ginny\n", timeout=5).exit()

@check50.check(exists)
def test9():
    """identifica correctamente sequences/9.txt"""
    check50.run("python3 adn.py databases/large.csv sequences/9.txt").stdout("^Draco", "Draco\n", timeout=5).exit()

@check50.check(exists)
def test10():
    """identifica correctamente sequences/10.txt"""
    check50.run("python3 adn.py databases/large.csv sequences/10.txt").stdout("^Albus", "Albus\n", timeout=5).exit()

@check50.check(exists)
def test11():
    """identifica correctamente sequences/11.txt"""
    check50.run("python3 adn.py databases/large.csv sequences/11.txt").stdout("^Hermione", "Hermione\n", timeout=5).exit()

@check50.check(exists)
def test12():
    """identifica correctamente sequences/12.txt"""
    check50.run("python3 adn.py databases/large.csv sequences/12.txt").stdout("^Lily", "Lily\n", timeout=5).exit()

@check50.check(exists)
def test13():
    """identifica correctamente sequences/13.txt"""
    check50.run("python3 adn.py databases/large.csv sequences/13.txt").stdout("^[Nn]o [Mm]atch\.?\n", "No match\n", timeout=5).exit()

@check50.check(exists)
def test14():
    """identifica correctamente sequences/14.txt"""
    check50.run("python3 adn.py databases/large.csv sequences/14.txt").stdout("^Severus", "Severus\n", timeout=5).exit()

@check50.check(exists)
def test15():
    """identifica correctamente sequences/15.txt"""
    check50.run("python3 adn.py databases/large.csv sequences/15.txt").stdout("^Sirius", "Sirius\n", timeout=5).exit()

@check50.check(exists)
def test16():
    """identifica correctamente sequences/16.txt"""
    check50.run("python3 adn.py databases/large.csv sequences/16.txt").stdout("^[Nn]o [Mm]atch\.?\n", "No match\n", timeout=5).exit()

@check50.check(exists)
def test17():
    """identifica correctamente sequences/17.txt"""
    check50.run("python3 adn.py databases/large.csv sequences/17.txt").stdout("^Harry", "Harry\n", timeout=5).exit()

@check50.check(exists)
def test18():
    """identifica correctamente sequences/18.txt"""
    check50.run("python3 adn.py databases/large.csv sequences/18.txt").stdout("^[Nn]o [Mm]atch\.?\n", "No match\n", timeout=5).exit()

@check50.check(exists)
def test19():
    """identifica correctamente sequences/19.txt"""
    check50.run("python3 adn.py databases/large.csv sequences/19.txt").stdout("^Fred", "Fred\n", timeout=5).exit()

@check50.check(exists)
def test20():
    """identifica correctamente sequences/20.txt"""
    check50.run("python3 adn.py databases/large.csv sequences/20.txt").stdout("^[Nn]o [Mm]atch\.?\n", "No match\n", timeout=5).exit()

