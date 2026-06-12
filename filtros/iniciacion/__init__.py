import check50
import check50.c
import re

SAMPLE_IMAGES = [

    # 0
    ["prueba con imagen de muestra 3x3 (niveles de posterización)",
    "primera fila: (0, 0, 0), (64, 64, 64), (128, 128, 128)",
    "segunda fila: (192, 0, 64), (0, 192, 128), (64, 0, 192)",
    "tercera fila: (145, 73, 200), (32, 96, 160), (100, 170, 210)"],

    # 1
    ["prueba con imagen de muestra 3x3 (colores variados)",
    "primera fila: (10, 20, 30), (40, 50, 60), (70, 80, 90)",
    "segunda fila: (110, 130, 140), (120, 140, 150), (130, 150, 160)",
    "tercera fila: (160, 170, 180), (180, 190, 200), (200, 210, 220)"],

    # 2
    ["prueba con imagen de muestra 4x4",
    "primera fila: (10, 20, 30), (40, 50, 60), (70, 80, 90), (100, 110, 120)",
    "segunda fila: (110, 130, 140), (120, 140, 150), (130, 150, 160), (140, 160, 170)",
    "tercera fila: (150, 160, 170), (160, 170, 180), (180, 190, 200), (200, 210, 220)",
    "cuarta fila: (50, 28, 90), (0, 0, 0), (192, 192, 192), (85, 85, 85)"],

    # 3 - para grayscale/reflect/blur (imagen original con 255)
    ["prueba con imagen de muestra 3x3",
    "primera fila: (255, 0, 0), (255, 0, 0), (255, 0, 0)",
    "segunda fila: (0, 255, 0), (0, 255, 0), (0, 255, 0)",
    "tercera fila: (0, 0, 255), (0, 0, 255), (0, 0, 255)"],

    # 4 - para grayscale/blur (imagen variada con 255)
    ["prueba con imagen de muestra 3x3",
    "primera fila: (10, 20, 30), (40, 50, 60), (70, 80, 90)",
    "segunda fila: (110, 130, 140), (120, 140, 150), (130, 150, 160)",
    "tercera fila: (200, 210, 220), (220, 230, 240), (240, 250, 255)"],

    # 5 - para grayscale/blur/reflect 4x4 (imagen con 255)
    ["prueba con imagen de muestra 4x4",
    "primera fila: (10, 20, 30), (40, 50, 60), (70, 80, 90), (100, 110, 120)",
    "segunda fila: (110, 130, 140), (120, 140, 150), (130, 150, 160), (140, 160, 170)",
    "tercera fila: (195, 204, 213), (205, 214, 223), (225, 234, 243), (245, 254, 253)",
    "cuarta fila: (50, 28, 90), (0, 0, 0), (255, 255, 255), (85, 85, 85)"],

    # 6 - para reflect 1x2
    ["testing with sample 1x2 image",
    "primera fila: (255, 0, 0), (0, 0, 255)"],

    # 7 - para reflect 1x3
    ["testing with sample 1x3 image",
    "primera fila: (255, 0, 0), (0, 255, 0), (0, 0, 255)"]
]

def SAMPLE_PIXEL(r, g, b):
    return f"probando con pixel ({r}, {g}, {b})"

def log(lines):
    if isinstance(lines, list):
        for line in lines:
            check50.log(line)
    else:
        check50.log(lines)

@check50.check()
def exists():
    """efectosvisuales.c existe"""
    check50.exists("efectosvisuales.c")
    check50.include("Makefile", "bmp.h", "efectosvisuales.h", "testing.c")

@check50.check(exists)
def compiles():
    """filtros compila"""
    check50.run("make").exit(0)

@check50.check(compiles)
def grayscale_single_pixel():
    """La escala de grises filtra correctamente un solo píxel con un promedio de números enteros."""
    log(SAMPLE_PIXEL(20, 40, 90))
    check50.run("./testing 0 0").stdout("50 50 50\n");
    pass

@check50.check(compiles)
def grayscale_rounding():
    """La escala de grises filtra correctamente un solo píxel sin promedio de números enteros."""
    log(SAMPLE_PIXEL(27, 28, 28))
    check50.run("./testing 0 1").stdout("28 28 28\n");
    pass

@check50.check(compiles)
def grayscale_gray():
    """La escala de grises deja solos los píxeles que ya son grises."""
    log(SAMPLE_PIXEL(50, 50, 50))
    check50.run("./testing 0 2").stdout("50 50 50\n");
    pass

@check50.check(compiles)
def grayscale_multi():
    """La escala de grises filtra correctamente una imagen simple de 3x3."""
    log(SAMPLE_IMAGES[3])
    check50.run("./testing 0 3").stdout("85 85 85\n" * 9);

@check50.check(compiles)
def grayscale3x3():
    """La escala de grises filtra correctamente imágenes de 3x3 más complejas."""
    log(SAMPLE_IMAGES[4])
    check50.run("./testing 0 4").stdout("".join([
        "20 20 20\n", "50 50 50\n", "80 80 80\n",
        "127 127 127\n", "137 137 137\n", "147 147 147\n",
        "210 210 210\n", "230 230 230\n", "248 248 248\n"
    ]))

@check50.check(compiles)
def grayscale4x4():
    """La escala de grises filtra correctamente la imagen 4x4."""
    log(SAMPLE_IMAGES[5])
    check50.run("./testing 0 5").stdout("".join([
        "20 20 20\n", "50 50 50\n", "80 80 80\n", "110 110 110\n",
        "127 127 127\n", "137 137 137\n", "147 147 147\n", "157 157 157\n",
        "204 204 204\n", "214 214 214\n", "234 234 234\n", "251 251 251\n",
        "56 56 56\n", "0 0 0\n", "255 255 255\n", "85 85 85\n"
    ]))

@check50.check(compiles)
def posterize_single_pixel():
    """Posterize filtra correctamente el píxel del ejemplo del enunciado."""
    log(SAMPLE_PIXEL(145, 73, 200))
    check50.run("./testing 1 0").stdout("128 64 192\n");
    pass

@check50.check(compiles)
def posterize_rounding_down():
    """Posterize redondea correctamente hacia el nivel inferior."""
    log(SAMPLE_PIXEL(20, 40, 90))
    check50.run("./testing 1 1").stdout("0 64 64\n");
    pass

@check50.check(compiles)
def posterize_exact_level():
    """Posterize deja solos los píxeles que ya están en un nivel exacto."""
    log(SAMPLE_PIXEL(64, 128, 192))
    check50.run("./testing 1 2").stdout("64 128 192\n");
    pass

@check50.check(compiles)
def posterize_multi():
    """Posterize filtra correctamente una imagen 3x3 que demuestra todos los niveles."""
    log(SAMPLE_IMAGES[0])
    check50.run("./testing 1 3").stdout("".join([
        "0 0 0\n", "64 64 64\n", "128 128 128\n",
        "192 0 64\n", "0 192 128\n", "64 0 192\n",
        "128 64 192\n", "0 128 128\n", "128 192 192\n"
    ]))

@check50.check(compiles)
def posterize3x3():
    """Posterize filtra correctamente imágenes 3x3 con colores variados."""
    log(SAMPLE_IMAGES[1])
    check50.run("./testing 1 4").stdout("".join([
        "0 0 0\n", "64 64 64\n", "64 64 64\n",
        "128 128 128\n", "128 128 128\n", "128 128 128\n",
        "128 192 192\n", "192 192 192\n", "192 192 192\n"
    ]))

@check50.check(compiles)
def posterize4x4():
    """Posterize filtra correctamente la imagen 4x4."""
    log(SAMPLE_IMAGES[2])
    check50.run("./testing 1 5").stdout("".join([
        "0 0 0\n", "64 64 64\n", "64 64 64\n", "128 128 128\n",
        "128 128 128\n", "128 128 128\n", "128 128 128\n", "128 128 192\n",
        "128 128 192\n", "128 192 192\n", "192 192 192\n", "192 192 192\n",
        "64 0 64\n", "0 0 0\n", "192 192 192\n", "64 64 64\n"
    ]))

@check50.check(compiles)
def reflect_row2():
    """Reflejar filtra correctamente imagen 1x2"""
    log(SAMPLE_IMAGES[6])
    check50.run("./testing 2 0").stdout("".join([
        "0 0 255\n", "255 0 0\n"
    ]))

@check50.check(compiles)
def reflect_row3():
    """Reflejar filtra correctamente imagen 1x3"""
    log(SAMPLE_IMAGES[7])
    check50.run("./testing 2 1").stdout("".join([
        "0 0 255\n", "0 255 0\n", "255 0 0\n"
    ]))

@check50.check(compiles)
def reflect_simple():
    """Reflejar filtra correctamente imagen que es su propia imagen reflejada"""
    log(SAMPLE_IMAGES[3])
    check50.run("./testing 2 2").stdout("".join([
        "255 0 0\n", "255 0 0\n", "255 0 0\n",
        "0 255 0\n", "0 255 0\n", "0 255 0\n",
        "0 0 255\n", "0 0 255\n", "0 0 255\n"
    ]))

@check50.check(compiles)
def reflect3():
    """Reflejar filtra correctamente imagen 3x3"""
    log(SAMPLE_IMAGES[4])
    check50.run("./testing 2 3").stdout("".join([
        "70 80 90\n", "40 50 60\n", "10 20 30\n",
        "130 150 160\n", "120 140 150\n", "110 130 140\n",
        "240 250 255\n", "220 230 240\n", "200 210 220\n"
    ]))

@check50.check(compiles)
def reflect4():
    """Reflejar filtra correctamente imagen 4x4"""
    log(SAMPLE_IMAGES[5])
    check50.run("./testing 2 4").stdout("".join([
        "100 110 120\n", "70 80 90\n", "40 50 60\n", "10 20 30\n",
        "140 160 170\n", "130 150 160\n", "120 140 150\n", "110 130 140\n",
        "245 254 253\n", "225 234 243\n", "205 214 223\n", "195 204 213\n",
        "85 85 85\n", "255 255 255\n", "0 0 0\n", "50 28 90\n"
    ]))

@check50.check(compiles)
def blur_middle():
    """Desenfocar filtra correctamente el píxel medio."""
    log(SAMPLE_IMAGES[4])
    check50.run("./testing 3 0").stdout("127 140 149\n")

@check50.check(compiles)
def blur_edge():
    """Desenfocar filtra correctamente el píxel en el borde"""
    log(SAMPLE_IMAGES[4])
    check50.run("./testing 3 1").stdout("80 95 105\n")

@check50.check(compiles)
def blur_corner():
    """Desenfocar filtra correctamente el píxel en la esquina"""
    log(SAMPLE_IMAGES[4])
    check50.run("./testing 3 2").stdout("70 85 95\n")

@check50.check(compiles)
def blur3():
    """Desenfocar filtra correctamente imagen 3x3"""
    log(SAMPLE_IMAGES[4])
    check50.run("./testing 3 3").stdout("".join([
        "70 85 95\n", "80 95 105\n", "90 105 115\n",
        "117 130 140\n", "127 140 149\n", "137 150 159\n",
        "163 178 188\n", "170 185 194\n", "178 193 201\n"
    ]))

@check50.check(compiles)
def blur4():
    """Desenfocar filtra correctamente imagen 4x4"""
    log(SAMPLE_IMAGES[5])
    check50.run("./testing 3 4").stdout("".join([
        "70 85 95\n", "80 95 105\n", "100 115 125\n", "110 125 135\n",
        "113 126 136\n", "123 136 145\n", "142 155 163\n", "152 165 173\n",
        "113 119 136\n", "143 151 164\n", "156 166 171\n", "180 190 194\n",
        "113 112 132\n", "155 156 171\n", "169 174 177\n", "203 207 209\n"
    ]))
