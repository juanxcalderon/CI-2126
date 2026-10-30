import re

import check50
import check50.c


# ─────────────────────────────────────────────────────────────────────────
#  Helpers / Ayudantes
#
#  The program echoes every candidate name while asking for votes
#  ("- Pedro: "), so a name showing up anywhere in the output proves
#  nothing. We only judge what is printed AFTER the last prompt.
#
#  El programa repite el nombre de cada candidato al pedir los votos
#  ("- Pedro: "), así que encontrar un nombre en la salida no prueba nada.
#  Solo se juzga lo que se imprime DESPUÉS del último mensaje de captura.
# ─────────────────────────────────────────────────────────────────────────

SECTORES = ["profesores", "estudiantes", "egresados", "empleados", "obreros"]


def entrada(votos_por_sector):
    """Una línea por voto: sector por sector, candidato por candidato."""
    return [str(v) for sector in votos_por_sector for v in sector]


def correr(candidatos, votos_por_sector):
    """Ejecuta el programa y devuelve (resultado_final, código_de_salida)."""
    proceso = check50.run("./elecciones " + " ".join(candidatos))
    for linea in entrada(votos_por_sector):
        proceso.stdin(linea, prompt=False)
    salida = proceso.stdout()
    codigo = proceso.exitcode  # stdout() already waited for the program to end

    # Everything after the last "- <last candidate>: " prompt is the verdict.
    # Todo lo que sigue al último "- <último candidato>: " es el veredicto.
    ultimo = f"- {candidatos[-1]}:"
    corte = salida.rfind(ultimo)
    if corte == -1:
        raise check50.Failure(
            "No se encontró la captura de votos del sector obrero. "
            "¿Modificó los mensajes del main?"
        )
    return salida[corte + len(ultimo):], codigo


def aparece(nombre, texto):
    return re.search(rf"\b{re.escape(nombre)}\b", texto) is not None


def esperar_ganador(candidatos, votos, ganador):
    final, codigo = correr(candidatos, votos)
    if not re.search(rf"Ganador:\s*{re.escape(ganador)}\b", final):
        raise check50.Mismatch(f"Ganador: {ganador}", final.strip())
    otros = [c for c in candidatos if c != ganador and aparece(c, final)]
    if otros:
        raise check50.Failure(
            f"Solo debe anunciarse a {ganador}, pero también aparece: {', '.join(otros)}"
        )
    if codigo != 0:
        raise check50.Failure(f"Se esperaba código de salida 0, se obtuvo {codigo}")


def esperar_segunda_ronda(candidatos, votos, pasan):
    final, codigo = correr(candidatos, votos)
    if re.search(r"(?i)ganador\s*:", final):
        raise check50.Failure(
            "Nadie supera el 50 % de los votos ponderados, así que no debe "
            f"declararse ganador. Salida: {final.strip()}"
        )
    faltan = [c for c in pasan if not aparece(c, final)]
    if faltan:
        raise check50.Failure(
            f"Debían pasar a segunda ronda {', '.join(pasan)}, pero falta: {', '.join(faltan)}"
        )
    sobran = [c for c in candidatos if c not in pasan and aparece(c, final)]
    if sobran:
        raise check50.Failure(
            f"{', '.join(sobran)} debía quedar eliminado y no mostrarse en la segunda ronda"
        )
    if codigo != 0:
        raise check50.Failure(f"Se esperaba código de salida 0, se obtuvo {codigo}")


def esperar_rechazo(voto_invalido):
    # The first vote typed is the invalid one; main must stop with code 4.
    # El primer voto es el inválido; el main debe terminar con código 4.
    proceso = check50.run("./elecciones Pedro Maria")
    proceso.stdin(voto_invalido, prompt=False)
    proceso.stdin("100", prompt=False)
    codigo = proceso.exit()
    if codigo != 4:
        raise check50.Failure(
            f"El voto «{voto_invalido}» debía rechazarse (código 4), "
            f"pero el programa terminó con código {codigo}"
        )


def iguales(votos_de_cada_candidato):
    """Mismos votos en los cinco sectores."""
    return [list(votos_de_cada_candidato) for _ in SECTORES]


# ─────────────────────────────────────────────────────────────────────────
#  Existencia y compilación / Existence and compilation
# ─────────────────────────────────────────────────────────────────────────

@check50.check()
def exists():
    """elecciones.c existe"""
    check50.exists("elecciones.c")


@check50.check(exists)
def compiles():
    """elecciones.c compila"""
    check50.c.compile("elecciones.c", exe_name="elecciones", lcs50=True)


# ─────────────────────────────────────────────────────────────────────────
#  Casos promedio / Typical cases
# ─────────────────────────────────────────────────────────────────────────

@check50.check(compiles)
def ejemplo_enunciado():
    """ejemplo del enunciado: Pedro gana con 52,14 % aunque Enrique tiene más votos sin ponderar"""
    # TVP: Pedro 52.1442 | Enrique 31.1738 | Maria 16.6820
    # Votos brutos / raw votes: Pedro 4629 < Enrique 4635
    esperar_ganador(["Pedro", "Enrique", "Maria"], [
        [290, 104, 37],
        [2356, 2012, 1009],
        [1041, 2101, 1087],
        [741, 214, 310],
        [201, 204, 99],
    ], "Pedro")


@check50.check(compiles)
def ejemplo_reglamento():
    """ejemplo del Reglamento: nadie supera 50 %, pasan Pedro y Maria"""
    # TVP: Pedro 43.05 | Enrique 24.55 | Maria 32.61 (tabla del Artículo 46)
    esperar_segunda_ronda(["Pedro", "Enrique", "Maria"], [
        [504, 159, 251],
        [1989, 793, 2114],
        [581, 1001, 1114],
        [399, 215, 198],
        [123, 267, 171],
    ], ["Pedro", "Maria"])


@check50.check(compiles)
def ganador_claro():
    """ganador claro en primera ronda (Pedro, 60 %)"""
    esperar_ganador(["Pedro", "Enrique", "Maria"], iguales([600, 200, 200]), "Pedro")


@check50.check(compiles)
def dos_candidatos():
    """dos candidatos, Maria gana directamente (60 %)"""
    esperar_ganador(["Pedro", "Maria"], iguales([400, 600]), "Maria")


@check50.check(compiles)
def ponderacion_por_sector():
    """pondera cada sector por separado y no suma votos brutos"""
    # Pedro sweeps the small professor sector; Maria wins the four big ones.
    # Raw votes favour Maria (5100 vs 2700) but the weighting gives Pedro 58.99 %.
    # Pedro arrasa en el sector profesoral, pequeño; Maria gana los otros cuatro.
    # Los votos brutos favorecen a Maria (5100 vs 2700), pero ponderado Pedro saca 58,99 %.
    esperar_ganador(["Pedro", "Maria"], [
        [300, 0],
        [600, 1400],
        [600, 1400],
        [600, 1300],
        [600, 1000],
    ], "Pedro")


# ─────────────────────────────────────────────────────────────────────────
#  Casos borde / Edge cases
# ─────────────────────────────────────────────────────────────────────────

@check50.check(compiles)
def empate_segundo_lugar():
    """empate en 2° lugar: Pedro, Enrique y Maria pasan a segunda ronda"""
    esperar_segunda_ronda(["Pedro", "Enrique", "Maria"], iguales([400, 300, 300]),
                          ["Pedro", "Enrique", "Maria"])


@check50.check(compiles)
def empate_primer_lugar():
    """empate en 1° lugar: pasan Pedro y Enrique, Maria queda eliminada"""
    esperar_segunda_ronda(["Pedro", "Enrique", "Maria"], iguales([400, 400, 200]),
                          ["Pedro", "Enrique"])


@check50.check(compiles)
def empate_total():
    """empate total: nadie es eliminado"""
    esperar_segunda_ronda(["Pedro", "Enrique", "Maria"], iguales([1000, 1000, 1000]),
                          ["Pedro", "Enrique", "Maria"])


@check50.check(compiles)
def cuatro_empate_segundo():
    """cuatro candidatos con triple empate en 2° lugar: pasan los cuatro"""
    esperar_segunda_ronda(["Pedro", "Enrique", "Maria", "Luis"], iguales([400, 200, 200, 200]),
                          ["Pedro", "Enrique", "Maria", "Luis"])


@check50.check(compiles)
def cincuenta_exacto():
    """50 % exacto no basta para ganar en primera vuelta"""
    # Pedro 50.00 | Enrique 25.00 | Maria 25.00 → no winner; tie for 2nd.
    esperar_segunda_ronda(["Pedro", "Enrique", "Maria"], iguales([500, 250, 250]),
                          ["Pedro", "Enrique", "Maria"])


@check50.check(compiles)
def margen_minimo():
    """Pedro gana con 50,04 % (los decimales no deben perderse)"""
    # A program that keeps weighted votes as int truncates this to 49 and fails.
    # Un programa que guarde los votos ponderados como int trunca esto a 49 y falla.
    esperar_ganador(["Pedro", "Enrique", "Maria"], [
        [501, 250, 249],
        [500, 250, 250],
        [500, 250, 250],
        [500, 250, 250],
        [500, 250, 250],
    ], "Pedro")


@check50.check(compiles)
def candidato_unico():
    """candidato único gana en una sola vuelta"""
    esperar_ganador(["Pedro"], [[800], [600], [450], [300], [200]], "Pedro")


@check50.check(compiles)
def diez_candidatos():
    """soporta hasta MAX_CANDIDATOS (10) candidatos"""
    nombres = ["Alicia", "Bruno", "Carlos", "Diana", "Elena",
               "Felix", "Gaby", "Hugo", "Ivan", "Julio"]
    esperar_segunda_ronda(nombres, iguales([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),
                          ["Ivan", "Julio"])


@check50.check(compiles)
def limite_superior_valido():
    """acepta 10000 votos (límite válido)"""
    esperar_ganador(["Pedro", "Maria"], iguales([10000, 5000]), "Pedro")


@check50.check(compiles)
def sector_sin_votos():
    """un sector sin votos aporta 0 % y la elección continúa (sin dividir entre cero)"""
    # Nobody votes in the workers' sector: its 10 % is lost (Art. 42).
    # Pedro gets 60 % of the remaining 90 % → 54 % and wins.
    # Nadie vota en el sector obrero: su 10 % se pierde (Art. 42).
    # Pedro saca el 60 % del 90 % restante → 54 % y gana.
    esperar_ganador(["Pedro", "Maria"], [
        [600, 400],
        [600, 400],
        [600, 400],
        [600, 400],
        [0, 0],
    ], "Pedro")


@check50.check(compiles)
def ningun_voto():
    """sin votos en ningún sector: empate total en 0 %, pasan todos"""
    esperar_segunda_ronda(["Pedro", "Enrique", "Maria"], iguales([0, 0, 0]),
                          ["Pedro", "Enrique", "Maria"])


# ─────────────────────────────────────────────────────────────────────────
#  Validación de entradas / Input validation
# ─────────────────────────────────────────────────────────────────────────

@check50.check(compiles)
def rechaza_negativos():
    """rechaza votos negativos"""
    esperar_rechazo("-1")


@check50.check(compiles)
def rechaza_mayor_maximo():
    """rechaza más de 10000 votos"""
    esperar_rechazo("10001")


@check50.check(compiles)
def rechaza_letras():
    """rechaza letras como votos"""
    esperar_rechazo("abc")
