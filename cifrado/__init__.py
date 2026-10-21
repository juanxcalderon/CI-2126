import re

import check50
import check50.c


def cifra(clave, texto, esperado):
    """Ejecuta ./cifrado con la clave, le da el texto y verifica el texto encriptado."""
    check50.run(f"./cifrado {clave}").stdin(texto).stdout(
        r"texto encriptado:\s*" + re.escape(esperado) + "\n",
        f"texto encriptado: {esperado}\n",
    ).exit(0)


@check50.check()
def exists():
    """cifrado.c existe"""
    check50.exists("cifrado.c")


@check50.check(exists)
def compiles():
    """cifrado.c compila"""
    check50.c.compile("cifrado.c", lcs50=True)


@check50.check(compiles)
def encrypt1():
    """encripta "HOLAMUNDO" como "LUOOMDHAN" usando SOL como clave"""
    cifra("SOL", "HOLAMUNDO", "LUOOMDHAN")


@check50.check(compiles)
def encrypt2():
    """encripta "HOLA MUNDO" como "LMDO NHAUO" usando SOL como clave"""
    cifra("SOL", "HOLA MUNDO", "LMDO NHAUO")


@check50.check(compiles)
def encrypt3():
    """encripta "HOLA MUNDO" como "LMDO NHAUO" usando sol como clave"""
    cifra("sol", "HOLA MUNDO", "LMDO NHAUO")


@check50.check(compiles)
def encrypt4():
    """encripta "HOLA MUNDO" como "LMDO NHAUO" usando SoL como clave"""
    cifra("SoL", "HOLA MUNDO", "LMDO NHAUO")


@check50.check(compiles)
def encrypt5():
    """ordena las columnas sin distinguir mayúsculas: encripta "abcdefgh" como "cgaebfdh" usando Bcad como clave"""
    cifra("Bcad", "abcdefgh", "cgaebfdh")


@check50.check(compiles)
def encrypt6():
    """preserva mayúsculas y signos: encripta "Ataque al Amanecer!" usando LIMON como clave"""
    cifra("LIMON", "Ataque al Amanecer!", "t meAeAcaaaru eqln!")


@check50.check(compiles)
def encrypt7():
    """encripta un texto más corto que la clave: "AB" como "BA" usando LIMON como clave"""
    cifra("LIMON", "AB", "BA")


@check50.check(compiles)
def encrypt8():
    """encripta con la última fila incompleta: "Shh... Don't tell!" usando PERLA como clave"""
    cifra("PERLA", "Shh... Don't tell!", ".neh tl.otS.'lhD !")


@check50.check(compiles)
def encrypt9():
    """encripta usando una clave de 26 letras"""
    cifra(
        "QWERTYUIOPASDFGHJKLZXCVBNM",
        "The quick brown fox jumps over the lazy dog",
        "bapuoyeew nd ocefgox sk  lTo rrzq ihmhvjut ",
    )


@check50.check(compiles)
def encrypt10():
    """mueve la ñ y las letras acentuadas como una sola letra: "Mañana, José!" usando SOL como clave"""
    cifra("SOL", "Mañana, José!", "ñaJéan sMa,o!")


@check50.check(compiles)
def encrypt11():
    """mueve ¿, ¡, ñ, tildes y diéresis como un solo carácter usando GATO como clave"""
    cifra(
        "GATO",
        "¿El niño pidió café? ¡Sí, y un pingüino!",
        "Eipóf¡ nnn¿n ia ,uii odc?í pü!lñi éSy go",
    )


@check50.check(compiles)
def encrypt12():
    """mueve caracteres de 3 bytes (€) como una sola letra usando CLAVE como clave"""
    cifra("CLAVE", "Cuesta 3€ o 5€, ¿vale?", "e35vCao et ,lu  ¿?s€€a")


@check50.check(compiles)
def encrypt13():
    """mueve caracteres de 4 bytes (emojis) como una sola letra usando SOL como clave"""
    cifra("SOL", "Hola 😀 mundo 🌎!", "l😀uo!o md🌎Ha n ")


@check50.check(compiles)
def handles_no_argv():
    """maneja la falta de clave de encriptación"""
    check50.run("./cifrado").exit(1)


@check50.check(compiles)
def handles_too_many_args():
    """maneja exceso de argumentos"""
    check50.run("./cifrado LIMON SOL").exit(1)


@check50.check(compiles)
def handles_short_key():
    """maneja una clave de menos de 3 letras"""
    check50.run("./cifrado OK").exit(1)


@check50.check(compiles)
def handles_empty_key():
    """maneja una clave vacía"""
    check50.run('./cifrado ""').exit(1)


@check50.check(compiles)
def handles_invalid_key_chars():
    """maneja caracteres no válidos en la clave de encriptación"""
    check50.run("./cifrado LIM0N").exit(1)


@check50.check(compiles)
def handles_enie_in_key():
    """maneja la ñ en la clave de encriptación (no es una letra del alfabeto inglés)"""
    check50.run("./cifrado PAÑO").exit(1)


@check50.check(compiles)
def handles_duplicate_chars_upper():
    """maneja caracteres duplicados en mayúsculas en la clave de encriptación"""
    check50.run("./cifrado CASA").exit(1)


@check50.check(compiles)
def handles_duplicate_chars_lower():
    """maneja caracteres duplicados en minúsculas en la clave de encriptación"""
    check50.run("./cifrado casa").exit(1)


@check50.check(compiles)
def handles_duplicate_mixed_case():
    """maneja un carácter duplicado de mayúsculas y minúsculas en la clave"""
    check50.run("./cifrado SOLs").exit(1)
