import check50
import check50.c


@check50.check()
def exists():
    """substitution.c existe"""
    check50.exists("substitution.c")


@check50.check(exists)
def compiles():
    """substitution.c compila"""
    check50.c.compile("substitution.c", lcs50=True)


@check50.check(compiles)
def encrypt1():
    """encripta de la "A" a la "Z" usando ZYXWVUTSRQPONMLKJIHGFEDCBA como clave"""
    check50.run("./substitution ZYXWVUTSRQPONMLKJIHGFEDCBA").stdin("A").stdout("ciphertext:\s*Z\n", "ciphertext: Z\n").exit(0)


@check50.check(compiles)
def encrypt2():
    """encripta de la "a" a la "z" usando ZYXWVUTSRQPONMLKJIHGFEDCBA como clave"""
    check50.run("./substitution ZYXWVUTSRQPONMLKJIHGFEDCBA").stdin("a").stdout("ciphertext:\s*z\n", "ciphertext: z\n").exit(0)


@check50.check(compiles)
def encrypt3():
    """encripta "ABC" como "NJQ" usando NJQSUYBRXMOPFTHZVAWCGILKED como clave"""
    check50.run("./substitution NJQSUYBRXMOPFTHZVAWCGILKED").stdin("ABC").stdout("ciphertext:\s*NJQ\n", "ciphertext: NJQ\n").exit(0)


@check50.check(compiles)
def encrypt4():
    """encripta "XyZ" como "KeD" usando NJQSUYBRXMOPFTHZVAWCGILKED como clave"""
    check50.run("./substitution NJQSUYBRXMOPFTHZVAWCGILKED").stdin("XyZ").stdout("ciphertext:\s*KeD\n", "ciphertext: KeD\n").exit(0)


@check50.check(compiles)
def encrypt5():
    """encripta "This is CS50" como "Cbah ah KH50" usando YUKFRNLBAVMWZTEOGXHCIPJSQD as clave"""
    check50.run("./substitution YUKFRNLBAVMWZTEOGXHCIPJSQD").stdin("This is CS50").stdout("ciphertext:\s*Cbah ah KH50\n", "ciphertext: Cbah ah KH50\n").exit(0)


@check50.check(compiles)
def encrypt6():
    """encripta "This is CS50" como "Cbah ah KH50" usando yukfrnlbavmwzteogxhcipjsqd como clave"""
    check50.run("./substitution yukfrnlbavmwzteogxhcipjsqd").stdin("This is CS50").stdout("ciphertext:\s*Cbah ah KH50\n", "ciphertext: Cbah ah KH50\n").exit(0)


@check50.check(compiles)
def encrypt7():
    """encripta "This is CS50" como "Cbah ah KH50" usando YUKFRNLBAVMWZteogxhcipjsqd como clave"""
    check50.run("./substitution YUKFRNLBAVMWZteogxhcipjsqd").stdin("This is CS50").stdout("ciphertext:\s*Cbah ah KH50\n", "ciphertext: Cbah ah KH50\n").exit(0)


@check50.check(compiles)
def encrypt8():
    """encripta todos los caracteres alfabéticos usando DWUSXNPQKEGCZFJBTLYROHIAVM como clave"""
    check50.run("./substitution DWUSXNPQKEGCZFJBTLYROHIAVM").stdin("The quick brown fox jumps over the lazy dog").stdout("ciphertext:\s*Rqx tokug wljif nja eozby jhxl rqx cdmv sjp\n", "ciphertext: Rqx tokug wljif nja eozby jhxl rqx cdmv sjp\n").exit(0)


@check50.check(compiles)
def encrypt9():
    """no cifra caracteres no-alfabéticos utilizando DWUSXNPQKEGCZFJBTLYROHIAVM como clave"""
    check50.run("./substitution DWUSXNPQKEGCZFJBTLYROHIAVM").stdin("Shh... Don't tell!").stdout("ciphertext:\s*Yqq... Sjf'r rxcc!\n", "ciphertext: Yqq... Sjf'r rxcc!\n").exit(0)


@check50.check(compiles)
def handles_no_argv():
    """maneja la falta de clave de encriptación"""
    check50.run("./substitution").exit(1)


@check50.check(compiles)
def handles_too_many_args():
    """maneja exceso de argumentos"""
    check50.run("./substitution abcdefghijklmnopqrstuvwxyz abc").exit(1)


@check50.check(compiles)
def handles_invalid_length():
    """maneja longitud de clave de encriptación no válida"""
    check50.run("./substitution QTXDGMKIPV").exit(1)


@check50.check(compiles)
def handles_invalid_key_chars():
    """maneja caracteres no válidos en la clave de encriptación"""
    check50.run("./substitution ZWGKPMJ^YISHFEXQON[DLUACVT").exit(1)


@check50.check(compiles)
def handles_duplicate_chars_upper():
    """maneja caracteres duplicados en mayúsculas en la clave de encriptación"""
    check50.run("./substitution FAZRDTMGQEJPWAXUSKVIYCLONH").exit(1)


@check50.check(compiles)
def handles_duplicate_chars_lower():
    """maneja caracteres duplicados en minúsculas en la clave de encriptación"""
    check50.run("./substitution fazrdtmgqejpwaxuskviyclonh").exit(1)


@check50.check(compiles)
def handles_multiple_duplicate_chars():
    """maneja múltiples caracteres duplicados en la clave de encriptación"""
    check50.run("./substitution MMCcEFGHIJKLMNOPqRqTUVWXeZ").exit(1)
