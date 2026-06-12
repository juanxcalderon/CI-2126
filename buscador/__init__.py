from check50 import *
import re
import shutil
from pathlib import Path

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def _reset_path(path):
    path = Path(path)
    if path.is_dir():
        shutil.rmtree(path)
    elif path.exists():
        path.unlink()


def _copy_fixture(name):
    src = FIXTURES / name
    corpus_dirs = [p for p in src.iterdir() if p.is_dir() and p.name.startswith("corpus_")]
    corpus_dir = corpus_dirs[0]
    _reset_path(corpus_dir.name)
    shutil.copytree(corpus_dir, corpus_dir.name)
    for file in src.iterdir():
        if file.is_file():
            shutil.copy2(file, file.name)
    return corpus_dir.name


def _check_output(self, corpus, consultas, esperado):
    expected = Path(esperado).read_text(encoding="utf-8")
    self.spawn(
        f"bash -c './buscador {corpus} {consultas} | grep -Ev \"^TIEMPO( DE EJECUCION DE| TOTAL:)\"'"
    ).stdout(re.escape(expected), expected).exit(0)


class Buscador(Checks):
    @check()
    def exists(self):
        """indice.c, indice.h y Makefile existen"""
        self.require("indice.c")
        self.require("indice.h")
        self.require("Makefile")

    @check("exists")
    def compiles(self):
        """buscador compila"""
        self.spawn("make buscador").exit(0)

    @check("compiles")
    def public_output(self):
        """produce la salida esperada para el corpus publico"""
        corpus = _copy_fixture("publico")
        _check_output(self, corpus, "consultas_publico.txt", "esperado_publico.txt")

    @check("compiles")
    def case_insensitive_and_order(self):
        """contains/documents son insensibles a mayusculas y documents devuelve nombres en orden lexicografico"""
        corpus = _copy_fixture("case_order")
        _check_output(self, corpus, "consultas_case_order.txt", "esperado_case_order.txt")

    @check("compiles")
    def punctuation(self):
        """ignora puntuacion al indexar palabras"""
        corpus = _copy_fixture("punctuation")
        _check_output(self, corpus, "consultas_punctuation.txt", "esperado_punctuation.txt")

    @check("compiles")
    def no_duplicate_docs_per_word(self):
        """documents no repite nombres cuando una palabra aparece muchas veces en el mismo archivo"""
        corpus = _copy_fixture("duplicates")
        _check_output(self, corpus, "consultas_duplicates.txt", "esperado_duplicates.txt")

    @check("compiles")
    def minimal_case(self):
        """maneja correctamente un corpus minimo"""
        corpus = _copy_fixture("minimal")
        _check_output(self, corpus, "consultas_minimal.txt", "esperado_minimal.txt")

    @check("compiles")
    def no_memory_errors_public(self):
        """no pierde memoria con el corpus publico"""
        corpus = _copy_fixture("publico")
        self.spawn(
            f"bash -c 'valgrind --leak-check=full --error-exitcode=1 ./buscador {corpus} consultas_publico.txt >/dev/null 2>&1'"
        ).exit(0)
