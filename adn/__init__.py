import check50


# ─────────────────────────────────────────────────────────────────
# Helper: construye el patrón regex para verificar el informe
# completo de 6 líneas. Usa [\s\S]* entre campos para ser flexible
# ante variaciones de espaciado, sin importar el orden exacto.
# ─────────────────────────────────────────────────────────────────
def patron_informe(nombre, porcentaje, analizados, coincidentes, nivel):
    # Escapa espacios en el nombre para el regex
    nombre_regex = nombre.replace(" ", r"\s+")
    return (
        r"Coincidencia encontrada:"
        r"[\s\S]*Nombre\s*:\s*" + nombre_regex +
        r"[\s\S]*Coincidencia STR\s*:\s*" + porcentaje.replace(".", r"\.") +
        r"%[\s\S]*STRs analizados\s*:\s*" + str(analizados) +
        r"[\s\S]*STRs coincidentes\s*:\s*" + str(coincidentes) +
        r"[\s\S]*Nivel de confianza\s*:\s*" + nivel
    )


def salida_esperada(nombre, porcentaje, analizados, coincidentes, nivel):
    return (
        f"Coincidencia encontrada:\n"
        f"Nombre            : {nombre}\n"
        f"Coincidencia STR  : {porcentaje}%\n"
        f"STRs analizados   : {analizados}\n"
        f"STRs coincidentes : {coincidentes}\n"
        f"Nivel de confianza: {nivel}\n"
    )


# ─────────────────────────────────────────────────────────────────
# CHECK 0 — El archivo existe
# ─────────────────────────────────────────────────────────────────
@check50.check()
def exists():
    """adn.py existe"""
    check50.exists("adn.py")
    check50.include("secuencias", "basesdedatos")


# ─────────────────────────────────────────────────────────────────
# CHECK uso — argumentos incorrectos
# ─────────────────────────────────────────────────────────────────
@check50.check(exists)
def test_uso_sin_args():
    """muestra mensaje de uso si no se pasan argumentos"""
    check50.run("python3 adn.py").stdout(
        r"[Uu]so\s*:\s*python\d?\s+adn\.py",
        "Uso: python adn.py data.csv secuencia.txt\n",
        timeout=5
    ).exit()


@check50.check(exists)
def test_uso_un_arg():
    """muestra mensaje de uso si se pasa solo un argumento"""
    check50.run("python3 adn.py basesdedatos/pequeno.csv").stdout(
        r"[Uu]so\s*:\s*python\d?\s+adn\.py",
        "Uso: python adn.py data.csv secuencia.txt\n",
        timeout=5
    ).exit()


# ─────────────────────────────────────────────────────────────────
# BASE PEQUEÑA — 4 secuencias (Alice, Bob, Charlie — nombres sin cambio)
# ─────────────────────────────────────────────────────────────────

@check50.check(exists)
def test1():
    """genera informe correcto para secuencias/1.txt (Bob, 100.00%, Alto)"""
    check50.run("python3 adn.py basesdedatos/pequeno.csv secuencias/1.txt").stdout(
        patron_informe("Bob", "100.00", 3, 3, "Alto"),
        salida_esperada("Bob", "100.00", 3, 3, "Alto"),
        timeout=5
    ).exit()


@check50.check(exists)
def test2():
    """genera informe correcto para secuencias/2.txt (Bob, 33.33%, Bajo)"""
    check50.run("python3 adn.py basesdedatos/pequeno.csv secuencias/2.txt").stdout(
        patron_informe("Bob", "33.33", 3, 1, "Bajo"),
        salida_esperada("Bob", "33.33", 3, 1, "Bajo"),
        timeout=5
    ).exit()


@check50.check(exists)
def test3():
    """genera informe correcto para secuencias/3.txt (Charlie, 66.67%, Bajo)"""
    check50.run("python3 adn.py basesdedatos/pequeno.csv secuencias/3.txt").stdout(
        patron_informe("Charlie", "66.67", 3, 2, "Bajo"),
        salida_esperada("Charlie", "66.67", 3, 2, "Bajo"),
        timeout=5
    ).exit()


@check50.check(exists)
def test4():
    """genera informe correcto para secuencias/4.txt (Alice, 100.00%, Alto)"""
    check50.run("python3 adn.py basesdedatos/pequeno.csv secuencias/4.txt").stdout(
        patron_informe("Alice", "100.00", 3, 3, "Alto"),
        salida_esperada("Alice", "100.00", 3, 3, "Alto"),
        timeout=5
    ).exit()


# ─────────────────────────────────────────────────────────────────
# BASE GRANDE — 16 secuencias (nombres completos de Harry Potter)
# ─────────────────────────────────────────────────────────────────

@check50.check(exists)
def test5():
    """genera informe correcto para secuencias/5.txt (Lavender Brown, 100.00%, Alto)"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/5.txt").stdout(
        patron_informe("Lavender Brown", "100.00", 8, 8, "Alto"),
        salida_esperada("Lavender Brown", "100.00", 8, 8, "Alto"),
        timeout=5
    ).exit()


@check50.check(exists)
def test6():
    """genera informe correcto para secuencias/6.txt (Luna Lovegood, 100.00%, Alto)"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/6.txt").stdout(
        patron_informe("Luna Lovegood", "100.00", 8, 8, "Alto"),
        salida_esperada("Luna Lovegood", "100.00", 8, 8, "Alto"),
        timeout=5
    ).exit()


@check50.check(exists)
def test7():
    """genera informe correcto para secuencias/7.txt (Ron Weasley, 100.00%, Alto)"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/7.txt").stdout(
        patron_informe("Ron Weasley", "100.00", 8, 8, "Alto"),
        salida_esperada("Ron Weasley", "100.00", 8, 8, "Alto"),
        timeout=5
    ).exit()


@check50.check(exists)
def test8():
    """genera informe correcto para secuencias/8.txt (Ginny Weasley, 100.00%, Alto)"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/8.txt").stdout(
        patron_informe("Ginny Weasley", "100.00", 8, 8, "Alto"),
        salida_esperada("Ginny Weasley", "100.00", 8, 8, "Alto"),
        timeout=5
    ).exit()


@check50.check(exists)
def test9():
    """genera informe correcto para secuencias/9.txt (Draco Malfoy, 100.00%, Alto)"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/9.txt").stdout(
        patron_informe("Draco Malfoy", "100.00", 8, 8, "Alto"),
        salida_esperada("Draco Malfoy", "100.00", 8, 8, "Alto"),
        timeout=5
    ).exit()


@check50.check(exists)
def test10():
    """genera informe correcto para secuencias/10.txt (Albus Dumbledore, 100.00%, Alto)"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/10.txt").stdout(
        patron_informe("Albus Dumbledore", "100.00", 8, 8, "Alto"),
        salida_esperada("Albus Dumbledore", "100.00", 8, 8, "Alto"),
        timeout=5
    ).exit()


@check50.check(exists)
def test11():
    """genera informe correcto para secuencias/11.txt (Hermione Granger, 100.00%, Alto)"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/11.txt").stdout(
        patron_informe("Hermione Granger", "100.00", 8, 8, "Alto"),
        salida_esperada("Hermione Granger", "100.00", 8, 8, "Alto"),
        timeout=5
    ).exit()


@check50.check(exists)
def test12():
    """genera informe correcto para secuencias/12.txt (Lily Potter, 100.00%, Alto)"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/12.txt").stdout(
        patron_informe("Lily Potter", "100.00", 8, 8, "Alto"),
        salida_esperada("Lily Potter", "100.00", 8, 8, "Alto"),
        timeout=5
    ).exit()


@check50.check(exists)
def test13():
    """genera informe correcto para secuencias/13.txt (Hermione Granger, 12.50%, Bajo)"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/13.txt").stdout(
        patron_informe("Hermione Granger", "12.50", 8, 1, "Bajo"),
        salida_esperada("Hermione Granger", "12.50", 8, 1, "Bajo"),
        timeout=5
    ).exit()


@check50.check(exists)
def test14():
    """genera informe correcto para secuencias/14.txt (Severus Snape, 100.00%, Alto)"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/14.txt").stdout(
        patron_informe("Severus Snape", "100.00", 8, 8, "Alto"),
        salida_esperada("Severus Snape", "100.00", 8, 8, "Alto"),
        timeout=5
    ).exit()


@check50.check(exists)
def test15():
    """genera informe correcto para secuencias/15.txt (Sirius Black, 100.00%, Alto)"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/15.txt").stdout(
        patron_informe("Sirius Black", "100.00", 8, 8, "Alto"),
        salida_esperada("Sirius Black", "100.00", 8, 8, "Alto"),
        timeout=5
    ).exit()


@check50.check(exists)
def test16():
    """genera informe correcto para secuencias/16.txt (Albus Dumbledore, 12.50%, Bajo)"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/16.txt").stdout(
        patron_informe("Albus Dumbledore", "12.50", 8, 1, "Bajo"),
        salida_esperada("Albus Dumbledore", "12.50", 8, 1, "Bajo"),
        timeout=5
    ).exit()


@check50.check(exists)
def test17():
    """genera informe correcto para secuencias/17.txt (Harry Potter, 100.00%, Alto)"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/17.txt").stdout(
        patron_informe("Harry Potter", "100.00", 8, 8, "Alto"),
        salida_esperada("Harry Potter", "100.00", 8, 8, "Alto"),
        timeout=5
    ).exit()


@check50.check(exists)
def test18():
    """genera informe correcto para secuencias/18.txt (Harry Potter, 87.50%, Medio)"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/18.txt").stdout(
        patron_informe("Harry Potter", "87.50", 8, 7, "Medio"),
        salida_esperada("Harry Potter", "87.50", 8, 7, "Medio"),
        timeout=5
    ).exit()


@check50.check(exists)
def test19():
    """genera informe correcto para secuencias/19.txt (Fred Weasley, 100.00%, Alto)"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/19.txt").stdout(
        patron_informe("Fred Weasley", "100.00", 8, 8, "Alto"),
        salida_esperada("Fred Weasley", "100.00", 8, 8, "Alto"),
        timeout=5
    ).exit()


@check50.check(exists)
def test20():
    """genera informe correcto para secuencias/20.txt (Petunia Dursley, 12.50%, Bajo)"""
    check50.run("python3 adn.py basesdedatos/grande.csv secuencias/20.txt").stdout(
        patron_informe("Petunia Dursley", "12.50", 8, 1, "Bajo"),
        salida_esperada("Petunia Dursley", "12.50", 8, 1, "Bajo"),
        timeout=5
    ).exit()
