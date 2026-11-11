import random
import shutil
from pathlib import Path

import check50

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def _preparar(nombre):
    """Copies one test case next to the student's program / Copia un caso de prueba junto al programa"""
    origen = FIXTURES / nombre
    repositorio = f"repositorio_{nombre}"
    shutil.rmtree(repositorio, ignore_errors=True)
    shutil.copytree(origen / repositorio, repositorio)
    for archivo in origen.iterdir():
        if archivo.is_file():
            shutil.copy2(archivo, archivo.name)
    return repositorio, f"consultas_{nombre}.txt", f"esperado_{nombre}.txt"


def _sin_tiempos(texto):
    """The time lines change on every run, so they are left out / Los tiempos cambian en cada ejecución"""
    lineas = [l.rstrip() for l in texto.replace("\r\n", "\n").split("\n") if not l.startswith("TIEMPO")]
    return "\n".join(lineas).strip()


def _comparar(nombre, timeout=10):
    repositorio, consultas, esperado = _preparar(nombre)
    check50.log(f"ejecutando ./buscador {repositorio} {consultas}")
    proceso = check50.run(f"./buscador {repositorio} {consultas}")
    salida = proceso.stdout(timeout=timeout)
    esperada = Path(esperado).read_text(encoding="utf-8")
    if _sin_tiempos(salida) != _sin_tiempos(esperada):
        raise check50.Mismatch(_sin_tiempos(esperada), _sin_tiempos(salida))
    if proceso.exitcode != 0:
        raise check50.Failure(f"se esperaba codigo de salida 0, no {proceso.exitcode}")


@check50.check()
def exists():
    """indice.c e indice.h existen"""
    check50.exists("indice.c", "indice.h")
    check50.include("buscador.c", "Makefile", "testing.c")


@check50.check(exists)
def compiles():
    """buscador compila"""
    check50.run("make buscador").exit(0)


@check50.check(compiles)
def publico():
    """produce la salida esperada con un repositorio sencillo"""
    _comparar("publico")


@check50.check(compiles)
def minimo():
    """maneja un repositorio de un solo documento y una palabra que no existe"""
    _comparar("minimo")


@check50.check(compiles)
def mayusculas():
    """es insensible a mayusculas y minusculas"""
    _comparar("mayusculas")


@check50.check(compiles)
def puntuacion():
    """los signos de puntuacion y los digitos separan palabras"""
    _comparar("puntuacion")


@check50.check(compiles)
def repetidos():
    """cada documento aparece una sola vez por palabra"""
    _comparar("repetidos")


@check50.check(compiles)
def acentos():
    """distingue las palabras con acento o enie de las que no lo llevan"""
    _comparar("acentos")


@check50.check(compiles)
def largas():
    """indexa palabras de 45 letras e ignora las mas largas"""
    _comparar("largas")


@check50.check(compiles)
def bordes():
    """maneja archivos vacios, sin salto de linea final y con saltos de Windows"""
    _comparar("bordes")


@check50.check(compiles)
def nombres():
    """documents devuelve los nombres en orden lexicografico, aunque tengan espacios o mayusculas"""
    _comparar("nombres")


@check50.check(compiles)
def inexistente():
    """load devuelve false si el repositorio no existe"""
    shutil.copy2(FIXTURES / "publico" / "consultas_publico.txt", "consultas_publico.txt")
    check50.run("./buscador repositorio_que_no_existe consultas_publico.txt").stdout(
        "No se pudo cargar", "No se pudo cargar repositorio_que_no_existe.\n").exit(1)


@check50.check(compiles)
def limite():
    """documents respeta max_docs y devuelve cuantos nombres copio"""
    repositorio, _, _ = _preparar("nombres")
    check50.run("clang -Wall -Wextra -Werror -std=c11 -o testing testing.c indice.c").exit(0)

    # "plaza" is in six documents, but only two fit / "plaza" está en seis documentos, pero solo caben dos
    esperada = "\n".join(["devolvio 2", "0: 007.txt", "1: A-League 2011-12.txt"]
                         + [f"{i}: (sin tocar)" for i in range(2, 8)] + ["size 3", "unload true"])
    salida = check50.run(f"./testing {repositorio} plaza 2").stdout(timeout=10)
    if salida.strip() != esperada:
        raise check50.Mismatch(esperada, salida.strip(), help="documents no debe copiar mas de max_docs nombres")

    # a word that is not in the index copies nothing / una palabra que no está no copia nada
    esperada = "\n".join(["devolvio 0"] + [f"{i}: (sin tocar)" for i in range(8)] + ["size 3", "unload true"])
    salida = check50.run(f"./testing {repositorio} ausente 5").stdout(timeout=10)
    if salida.strip() != esperada:
        raise check50.Mismatch(esperada, salida.strip(), help="si la palabra no esta, documents debe devolver 0")


@check50.check(compiles)
def rapidez():
    """indexa y consulta un repositorio mediano en menos de 8 segundos"""
    # A good hash function takes well under a second here; the one in the distribution code takes over 20.
    # Una buena función hash tarda mucho menos de un segundo aquí; la del código de distribución, más de 20.
    # 120 documents of 5000 words each, taken from 60000 different words (always the same ones).
    # 120 documentos de 5000 palabras cada uno, tomadas de 60000 palabras distintas (siempre las mismas).
    azar = random.Random(2126)
    letras = "abcdefghijklmnopqrstuvwxyz"
    vocabulario = set()
    while len(vocabulario) < 60000:
        vocabulario.add("".join(azar.choice(letras) for _ in range(azar.randint(3, 11))))
    vocabulario = sorted(vocabulario)
    carpeta = Path("repositorio_mediano")
    shutil.rmtree(carpeta, ignore_errors=True)
    carpeta.mkdir()
    presentes = {}
    for d in range(120):
        nombre = f"doc{d:03d}.txt"
        palabras = [azar.choice(vocabulario) for _ in range(5000)]
        for p in palabras:
            presentes.setdefault(p, set()).add(nombre)
        (carpeta / nombre).write_text(" ".join(palabras) + "\n")
    consultas = [azar.choice(vocabulario) for _ in range(300)]
    Path("consultas_mediano.txt").write_text("\n".join(consultas) + "\n")

    esperada = ["RESULTADOS", ""]
    for q in consultas:
        esperada.append(q + ":" + "".join(" " + n for n in sorted(presentes.get(q, ()))))
    esperada += ["", f"PALABRAS INDEXADAS:                 {len(presentes)}",
                 f"CONSULTAS PROCESADAS:               {len(consultas)}"]
    esperada = "\n".join(esperada)

    try:
        salida = check50.run("./buscador repositorio_mediano consultas_mediano.txt").stdout(timeout=8)
    except check50.Failure:
        raise check50.Failure("el programa tardo mas de 8 segundos",
                              help="revisa tu funcion hash, el valor de N y como insertas los documentos")
    if _sin_tiempos(salida) != esperada:
        raise check50.Failure("la salida con el repositorio mediano no es la esperada")


@check50.check(compiles)
def memoria():
    """libera toda la memoria y no comete errores de memoria"""
    repositorio, consultas, _ = _preparar("acentos")
    check50.run(
        f"valgrind --leak-check=full --errors-for-leak-kinds=all --error-exitcode=9 -q ./buscador {repositorio} {consultas}"
    ).exit(0, timeout=30)
