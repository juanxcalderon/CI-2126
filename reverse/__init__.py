import check50
import check50.c


@check50.check()
def exists():
    """reverse.c existe"""
    check50.include("input.wav")
    check50.include("wav.h")
    check50.exists("reverse.c")


@check50.check(exists)
def compiles():
    """reverse.c compila"""
    check50.c.compile("reverse.c", lcs50=True)


@check50.check(compiles)
def test_nofile():
    """reverse.c maneja la falta de archivo de entrada"""
    check50.run("./reverse").exit(1)


@check50.check(compiles)
def test_output_file():
    """reverse.c crea un archivo de salida"""
    check50.run("./reverse input.wav output.wav").exit(0, timeout=10)
    check50.exists("output.wav")


@check50.check(test_output_file)
def test_header():
    """reverse.c escribe el encabezado WAV en el archivo de salida"""
    check50.run("./reverse input.wav output.wav").exit(0, timeout=10)
    with open("output.wav", "rb") as f:
        f.seek(8)
        for b in [b'W', b'A', b'V', b'E']:
            if f.read(1) != b:
                raise check50.Failure("el archivo de salida no tiene firma de archivo WAV")


@check50.check(test_header)
def test_reverses_audio():
    """reverse.c invierte la escala ascendente"""
    check50.run("./reverse input.wav output.wav").exit(0, timeout=10)
    file_hash = check50.hash("output.wav")
    if file_hash != "bb4a927734bee48387e820ebf0ad3cf67fa5db88bf8c11eea6b61162174ec02f":
        
        # Correct, except for final block
        if file_hash == "d7beb50a997b78e257cf77e1c6fa0bf835e8e59f86aa082a7a35f7ccc8d307b4":
            raise check50.Failure("el archivo no se invierte como se especifica", help="¿Olvidaste incluir el último bloque del archivo de entrada?")
            
        # Includes reversed header (whether missing final block or not)
        elif file_hash == "f206747786873dd0c565b048a2da1eb23d925cb862dd6c4d151a2978f6090c13" or file_hash == "e1e69515128debe5575995e89f4003bc44e2d5a362afa7314e81b621e9620934":
            raise check50.Failure("el archivo no se invierte como se especifica", help="¡Parece que incluiste un encabezado invertido al final de tu archivo!")
        
        # All other cases
        raise check50.Failure("el archivo no se invierte como se especifica")
