import check50
import check50.c


# ─────────────────────────────────────────────
#  Helper
# ─────────────────────────────────────────────

def stdin_votos(votos_por_sector):
    """
    Construye la secuencia de stdin.
    votos_por_sector: lista de 5 listas (profesores, estudiantes,
    egresados, empleados, obreros); cada sublista tiene los votos
    de cada candidato en ese sector, en el mismo orden en que
    aparecen como argumentos de línea de comandos.
    """
    lines = []
    for sector in votos_por_sector:
        for v in sector:
            lines.append(str(v))
    return "\n".join(lines)


# ─────────────────────────────────────────────
#  Existencia y compilación
# ─────────────────────────────────────────────

@check50.check()
def exists():
    """elecciones.c existe"""
    check50.exists("elecciones.c")


@check50.check(exists)
def compiles():
    """elecciones.c compila"""
    check50.c.compile("elecciones.c", exe_name="elecciones")


# ─────────────────────────────────────────────
#  CP-1  Ganador claro en primera ronda — 3 candidatos
#
#  ./elecciones Pedro Enrique Maria
#  Todos los sectores con Vv=1000 (mismos votos en los 5 sectores):
#    Pedro=600, Enrique=200, Maria=200
#  TVP: Pedro=64.25%, Enrique=17.875%, Maria=17.875%
#  SALIDA ESPERADA: Ganador: Pedro
# ─────────────────────────────────────────────

@check50.check(compiles)
def cp1_ganador_claro_primera_ronda():
    """CP-1: ganador claro en primera ronda (Pedro, 64.25%)"""
    stdin = stdin_votos([
        [600, 200, 200],  # profesores  Vv=1000
        [600, 200, 200],  # estudiantes Vv=1000
        [600, 200, 200],  # egresados   Vv=1000
        [600, 200, 200],  # empleados   Vv=1000
        [600, 200, 200],  # obreros     Vv=1000
    ])
    check50.run("./elecciones Pedro Enrique Maria") \
        .stdin(stdin) \
        .stdout(r"(?i)Pedro", regex=True) \
        .exit(0)


# ─────────────────────────────────────────────
#  CP-2  Segunda ronda — ejemplo del enunciado
#
#  ./elecciones Pedro Enrique Maria
#  TVP: Pedro=42.98%, Enrique=24.50%, Maria=32.52%
#  → nadie supera 50% → segunda ronda: Pedro y Maria
# ─────────────────────────────────────────────

@check50.check(compiles)
def cp2_segunda_ronda_ejemplo_enunciado():
    """CP-2: segunda ronda — ejemplo del enunciado (Pedro y Maria pasan)"""
    stdin = stdin_votos([
        [504, 159, 251],    # profesores  Vv=914
        [1989, 793, 2114],  # estudiantes Vv=4896
        [581, 1001, 1114],  # egresados   Vv=2696
        [399, 215, 198],    # empleados   Vv=812
        [123, 267, 171],    # obreros     Vv=561
    ])
    run = check50.run("./elecciones Pedro Enrique Maria")
    output = run.stdin(stdin).stdout()
    if "Pedro" not in output:
        raise check50.Failure("Se esperaba que Pedro apareciera en la segunda ronda")
    if "Maria" not in output:
        raise check50.Failure("Se esperaba que Maria apareciera en la segunda ronda")


# ─────────────────────────────────────────────
#  CP-4  Dos candidatos — uno gana directamente
#
#  ./elecciones Pedro Maria
#  Todos los sectores: Pedro=600, Maria=400  → Vv=1000
#  TVP: Pedro=60%, Maria=40%
#  SALIDA ESPERADA: Ganador: Pedro
# ─────────────────────────────────────────────

@check50.check(compiles)
def cp4_dos_candidatos_gana_directo():
    """CP-4: dos candidatos, Pedro gana directamente (60%)"""
    stdin = stdin_votos([
        [600, 400],  # profesores
        [600, 400],  # estudiantes
        [600, 400],  # egresados
        [600, 400],  # empleados
        [600, 400],  # obreros
    ])
    check50.run("./elecciones Pedro Maria") \
        .stdin(stdin) \
        .stdout(r"(?i)Pedro", regex=True) \
        .exit(0)


# ─────────────────────────────────────────────
#  CB-1  Empate en 2° lugar → los 3 pasan a 2ª ronda
#
#  ./elecciones Pedro Enrique Maria
#  Todos los sectores: Pedro=400, Enrique=300, Maria=300  → Vv=1000
#  TVP: Pedro=40%, Enrique=30%, Maria=30%
#  Enrique y Maria empatados en 2° → los 3 pasan
# ─────────────────────────────────────────────

@check50.check(compiles)
def cb1_empate_segundo_lugar_tres_pasan():
    """CB-1: empate en 2° lugar → Pedro, Enrique y Maria pasan a segunda ronda"""
    stdin = stdin_votos([
        [400, 300, 300],  # profesores
        [400, 300, 300],  # estudiantes
        [400, 300, 300],  # egresados
        [400, 300, 300],  # empleados
        [400, 300, 300],  # obreros
    ])
    run = check50.run("./elecciones Pedro Enrique Maria")
    output = run.stdin(stdin).stdout()
    for nombre in ["Pedro", "Enrique", "Maria"]:
        if nombre not in output:
            raise check50.Failure(
                f"Se esperaba que {nombre} apareciera (empate en 2° lugar)"
            )


# ─────────────────────────────────────────────
#  CB-2  Empate en 1° lugar → solo los dos primeros pasan
#
#  ./elecciones Pedro Enrique Maria
#  Todos los sectores: Pedro=400, Enrique=400, Maria=200  → Vv=1000
#  TVP: Pedro=40%, Enrique=40%, Maria=20%
#  Pedro y Enrique empatados en 1° → pasan; Maria eliminada
# ─────────────────────────────────────────────

@check50.check(compiles)
def cb2_empate_primer_lugar_dos_pasan():
    """CB-2: empate en 1° lugar → Pedro y Enrique pasan, Maria eliminada"""
    stdin = stdin_votos([
        [400, 400, 200],  # profesores
        [400, 400, 200],  # estudiantes
        [400, 400, 200],  # egresados
        [400, 400, 200],  # empleados
        [400, 400, 200],  # obreros
    ])
    run = check50.run("./elecciones Pedro Enrique Maria")
    output = run.stdin(stdin).stdout()
    if "Pedro" not in output:
        raise check50.Failure("Pedro (1° empatado) debería pasar a segunda ronda")
    if "Enrique" not in output:
        raise check50.Failure("Enrique (1° empatado) debería pasar a segunda ronda")


# ─────────────────────────────────────────────
#  CB-3  Empate total — nadie es eliminado
#
#  ./elecciones Pedro Enrique Maria
#  Todos los sectores: Pedro=1000, Enrique=1000, Maria=1000  → Vv=3000
#  TVP: Pedro=33.33%, Enrique=33.33%, Maria=33.33%
#  Empate perfecto → ninguno eliminado, los 3 aparecen
# ─────────────────────────────────────────────

@check50.check(compiles)
def cb3_empate_total_nadie_eliminado():
    """CB-3: empate total → ninguno eliminado, los 3 aparecen en pantalla"""
    stdin = stdin_votos([
        [1000, 1000, 1000],  # profesores
        [1000, 1000, 1000],  # estudiantes
        [1000, 1000, 1000],  # egresados
        [1000, 1000, 1000],  # empleados
        [1000, 1000, 1000],  # obreros
    ])
    run = check50.run("./elecciones Pedro Enrique Maria")
    output = run.stdin(stdin).stdout()
    for nombre in ["Pedro", "Enrique", "Maria"]:
        if nombre not in output:
            raise check50.Failure(
                f"Se esperaba que {nombre} apareciera (empate total, nadie eliminado)"
            )


# ─────────────────────────────────────────────
#  CB-5  Gana por margen mínimo — 50.04% (1 voto de diferencia vs 50.00%)
#
#  ./elecciones Pedro Enrique Maria
#  Profesores: Pedro=501, Enrique=250, Maria=249  → Vv=1000
#  Demás sectores: Pedro=500, Enrique=250, Maria=250  → Vv=1000
#  TVP: Pedro=50.04%, Enrique=25.00%, Maria=24.96%
#  SALIDA ESPERADA: Ganador: Pedro  (50.04% > 50%)
# ─────────────────────────────────────────────

@check50.check(compiles)
def cb5_gana_margen_minimo():
    """CB-5: Pedro gana con 50.04% (un solo voto sobre el umbral)"""
    stdin = stdin_votos([
        [501, 250, 249],  # profesores  (1 voto extra a Pedro)
        [500, 250, 250],  # estudiantes
        [500, 250, 250],  # egresados
        [500, 250, 250],  # empleados
        [500, 250, 250],  # obreros
    ])
    check50.run("./elecciones Pedro Enrique Maria") \
        .stdin(stdin) \
        .stdout(r"(?i)Pedro", regex=True) \
        .exit(0)


# ─────────────────────────────────────────────
#  CB-6  Un único candidato — una sola vuelta (Art. 45, Parágrafo Segundo)
#
#  ./elecciones Pedro
#  Profesores=800, Estudiantes=600, Egresados=450,
#  Empleados=300, Obreros=200
#  TVP: Pedro=100%
#  SALIDA ESPERADA: Ganador: Pedro
# ─────────────────────────────────────────────

@check50.check(compiles)
def cb6_candidato_unico_gana():
    """CB-6: candidato único gana directamente (una sola vuelta)"""
    stdin = stdin_votos([
        [800],  # profesores
        [600],  # estudiantes
        [450],  # egresados
        [300],  # empleados
        [200],  # obreros
    ])
    check50.run("./elecciones Pedro") \
        .stdin(stdin) \
        .stdout(r"(?i)Pedro", regex=True) \
        .exit(0)


# ─────────────────────────────────────────────
#  MAX_CANDIDATOS — 10 candidatos (límite máximo)
#
#  ./elecciones Alice Bob Carlos Diana Elena Frank Gaby Hugo Ivan Julio
#  Todos los sectores: Alice=1000, resto=100  → Vv=1900
#  TVP de Alice >> 50% → gana en primera ronda
# ─────────────────────────────────────────────

@check50.check(compiles)
def max_candidatos():
    """soporta hasta MAX_CANDIDATOS (10) candidatos"""
    sector = [1000] + [100] * 9  # A domina, los otros 9 con 100 c/u
    stdin = stdin_votos([sector] * 5)
    check50.run("./elecciones Alice Bob Carlos Diana Elena Frank Gaby Hugo Ivan Julio") \
        .stdin(stdin) \
        .stdout(r"(?i)Alice", regex=True) \
        .exit(0)
