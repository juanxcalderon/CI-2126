import check50

@check50.check()
def exists():
    """adn.py existe"""
    check50.exists("adn.py")
    check50.include("secuencias", "basesdedatos")

@check50.check(exists)
def test1():
    """identifica correctamente secuencias/1.txt"""
    check50.run("python3 adn.py basesdedatos/pequeno.csv secuencias/1.txt").stdout("^Bob", "Bob\n", timeout=5).exit()

@check50.check(exists)
def test2():
    """identifica correctamente secuencias/2.txt"""
    check50.run("python3 adn.py basesdedatos/pequeno.csv secuencias/2.txt").stdout("^[Ss]in [Cc]oincidencia\.?\n", "Sin coincidencia\n", timeout=5).exit()

@check50.check(exists)
def test3():
    """identifica correctamente secuencias/3.txt"""
    check50.run("python3 adn.py basesdedatos/pequeno.csv secuencias/3.txt").stdout("^[Ss]in [Cc]oincidencia\.?\n", "Sin coincidencia\n", timeout=5).exit()

@check50.check(exists)
def test4():
    """identifica correctamente secuencias/4.txt"""
    check50.run("python3 adn.py basesdedatos/pequeno.csv secuencias/4.txt").stdout("^Alice", "Alice\n", timeout=5).exit()

@check50.check(exists)
def test5():
    """identifica correctamente secuencias/5.txt"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/5.txt").stdout("^Lavender", "Lavender\n", timeout=5).exit()

@check50.check(exists)
def test6():
    """identifica correctamente secuencias/6.txt"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/6.txt").stdout("^Luna", "Luna\n", timeout=5).exit()

@check50.check(exists)
def test7():
    """identifica correctamente secuencias/7.txt"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/7.txt").stdout("^Ron", "Ron\n", timeout=5).exit()

@check50.check(exists)
def test8():
    """identifica correctamente secuencias/8.txt"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/8.txt").stdout("^Ginny", "Ginny\n", timeout=5).exit()

@check50.check(exists)
def test9():
    """identifica correctamente secuencias/9.txt"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/9.txt").stdout("^Draco", "Draco\n", timeout=5).exit()

@check50.check(exists)
def test10():
    """identifica correctamente secuencias/10.txt"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/10.txt").stdout("^Albus", "Albus\n", timeout=5).exit()

@check50.check(exists)
def test11():
    """identifica correctamente secuencias/11.txt"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/11.txt").stdout("^Hermione", "Hermione\n", timeout=5).exit()

@check50.check(exists)
def test12():
    """identifica correctamente secuencias/12.txt"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/12.txt").stdout("^Lily", "Lily\n", timeout=5).exit()

@check50.check(exists)
def test13():
    """identifica correctamente secuencias/13.txt"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/13.txt").stdout("^[Ss]in [Cc]oincidencia\.?\n", "Sin coincidencia\n", timeout=5).exit()

@check50.check(exists)
def test14():
    """identifica correctamente secuencias/14.txt"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/14.txt").stdout("^Severus", "Severus\n", timeout=5).exit()

@check50.check(exists)
def test15():
    """identifica correctamente secuencias/15.txt"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/15.txt").stdout("^Sirius", "Sirius\n", timeout=5).exit()

@check50.check(exists)
def test16():
    """identifica correctamente secuencias/16.txt"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/16.txt").stdout("^[Ss]in [Cc]oincidencia\.?\n", "Sin coincidencia\n", timeout=5).exit()

@check50.check(exists)
def test17():
    """identifica correctamente secuencias/17.txt"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/17.txt").stdout("^Harry", "Harry\n", timeout=5).exit()

@check50.check(exists)
def test18():
    """identifica correctamente secuencias/18.txt"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/18.txt").stdout("^[Ss]in [Cc]oincidencia\.?\n", "Sin coincidencia\n", timeout=5).exit()

@check50.check(exists)
def test19():
    """identifica correctamente secuencias/19.txt"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/19.txt").stdout("^Fred", "Fred\n", timeout=5).exit()

@check50.check(exists)
def test20():
    """identifica correctamente secuencias/20.txt"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/20.txt").stdout("^[Ss]in [Cc]oincidencia\.?\n", "Sin coincidencia\n", timeout=5).exit()

