import check50
import check50.c

@check50.check()
def exists():
    """caesar.c existe."""
    check50.exists("caesar.c")

@check50.check(exists)
def compiles():
    """caesar.c compila."""
    check50.c.compile("caesar.c", lcs50=True)

@check50.check(compiles)
def encrypts_a_as_b():
    """encripta "a"como "b" usando 1 como clave"""
    check50.run("./caesar 1").stdin("a").stdout("[Cc]iphertext:\s*b\n", "ciphertext: b\n").exit(0)

@check50.check(compiles)
def encrypts_barfoo_as_yxocll():
    """encripta "barfoo" como "yxocll" usando 23 como clave"""
    check50.run("./caesar 23").stdin("barfoo").stdout("[Cc]iphertext:\s*yxocll\n", "ciphertext: yxocll\n").exit(0)

@check50.check(compiles)
def encrypts_BARFOO_as_EDUIRR():
    """encripta "BARFOO" como "EDUIRR" usando 3 como clave"""
    check50.run("./caesar 3").stdin("BARFOO").stdout("[Cc]iphertext:\s*EDUIRR\n", "ciphertext: EDUIRR\n").exit(0)

@check50.check(compiles)
def encrypts_BaRFoo_FeVJss():
    """encripta "BaRFoo" como "FeVJss" usando 4 como clave"""
    check50.run("./caesar 4").stdin("BaRFoo").stdout("[Cc]iphertext:\s*FeVJss\n", "ciphertext: FeVJss\n").exit(0)

@check50.check(compiles)
def encrypts_barfoo_as_onesbb():
    """encripta "barfoo" como "onesbb" usando 65 como clave"""
    check50.run("./caesar 65").stdin("barfoo").stdout("[Cc]iphertext:\s*onesbb\n", "ciphertext: onesbb\n").exit(0)

@check50.check(compiles)
def checks_for_handling_non_alpha():
    """encripta "world, say hello!" como "iadxp, emk tqxxa!" usando 12 como clave"""
    check50.run("./caesar 12").stdin("world, say hello!").stdout("[Cc]iphertext:\s*iadxp, emk tqxxa!\n", "ciphertext: iadxp, emk tqxxa!\n").exit(0)

@check50.check(compiles)
def handles_no_argv():
    """maneja la ausencia de argv[1]"""
    check50.run("./caesar").exit(1)
    
@check50.check(compiles)
def handles_non_numeric_argv():
    """maneja claves no-numéricas"""
    check50.run("./caesar 2x").exit(1)
    
@check50.check(compiles)
def too_many_args():
    """maneja exceso de argumentos"""
    check50.run("./caesar 1 2").exit(1)
