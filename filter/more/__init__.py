import check50
import check50.c
import re

SAMPLE_IMAGES = [

    # 0
    ["prueba con imagen de muestra 3x3",
    "first row: (255, 0, 0), (255, 0, 0), (255, 0, 0)",
    "second row: (0, 255, 0), (0, 255, 0), (0, 0, 255)",
    "third row: (0, 0, 255), (0, 0, 255), (0, 0, 255)"],

    # 1
    ["prueba con imagen de muestra 3x3",
    "first row: (10, 20, 30), (40, 50, 60), (70, 80, 90)",
    "second row: (110, 130, 140), (120, 140, 150), (130, 150, 160)",
    "third row: (200, 210, 220), (220, 230, 240), (240, 250, 255)"],

    # 2
    ["prueba con imagen de muestra 4x4",
    "first row: (10, 20, 30), (40, 50, 60), (70, 80, 90), (100, 110, 120)",
    "second row: (110, 130, 140), (120, 140, 150), (130, 150, 160), (140, 160, 170)",
    "third row: (195, 204, 213), (205, 214, 223), (225, 234, 243), (245, 254, 253)",
    "fourth row: (50, 28, 90), (0, 0, 0), (255, 255, 255), (85, 85, 85)"],

    # 3
    ["prueba con imagen de muestra 1x2",
    "first row: (255, 0, 0), (0, 0, 255)"],

    # 4
    ["prueba con imagen de muestra 1x3",
    "first row: (255, 0, 0), (0, 255, 0), (0, 0, 255)"],

    # 5
    ["prueba con imagen de muestra 3x3",
    "first row: (0, 10, 25), (0, 10, 30), (40, 60, 80)",
    "second row: (20, 30, 90), (30, 40, 100), (80, 70, 90)",
    "third row: (20, 20, 40), (30, 10, 30), (50, 40, 10)"],

    # 6
    ["prueba con imagen de muestra 3x3",
    "first row: (0, 10, 25), (0, 10, 30), (40, 60, 80), (50, 60, 80)",
    "second row: (20, 30, 90), (30, 40, 100), (80, 70, 90), (80, 80, 90)",
    "third row: (20, 20, 40), (30, 10, 30), (50, 40, 10), (50, 40, 100)",
    "fourth row: (50, 20, 40), (50, 20, 40), (50, 40, 80), (50, 40, 80)"]
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
    """helpers.c existe"""
    check50.exists("helpers.c")
    check50.include("Makefile", "bmp.h", "helpers.h", "testing.c")

@check50.check(exists)
def compiles():
    """filter compila"""
    check50.run("make").exit(0)

@check50.check(compiles)
def grayscale_single_pixel():
    """La escala de grises filtra correctamente un solo píxel con un promedio de números enteros."""
    log(SAMPLE_PIXEL(20, 40, 90))
    check50.run("./testing 0 0").stdout("50 50 50\n");
    pass

@check50.check(compiles)
def grayscale_rounding():
    """La escala de grises filtra correctamente un solo píxel sin un promedio de números enteros."""
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
    log(SAMPLE_IMAGES[0])
    check50.run("./testing 0 3").stdout("85 85 85\n" * 9);

@check50.check(compiles)
def grayscale3x3():
    """La escala de grises filtra correctamente imágenes de 3x3 más complejas."""
    log(SAMPLE_IMAGES[1])
    check50.run("./testing 0 4").stdout("".join([
        "20 20 20\n", "50 50 50\n", "80 80 80\n",
        "127 127 127\n", "137 137 137\n", "147 147 147\n",
        "210 210 210\n", "230 230 230\n", "248 248 248\n"
    ]))


@check50.check(compiles)
def grayscale4x4():
    """La escala de grises filtra correctamente la imagen 4x4."""
    log(SAMPLE_IMAGES[2])
    check50.run("./testing 0 5").stdout("".join([
        "20 20 20\n", "50 50 50\n", "80 80 80\n", "110 110 110\n",
        "127 127 127\n", "137 137 137\n", "147 147 147\n", "157 157 157\n",
        "204 204 204\n", "214 214 214\n", "234 234 234\n", "251 251 251\n",
        "56 56 56\n", "0 0 0\n", "255 255 255\n", "85 85 85\n"
    ]))

@check50.check(compiles)
def reflect_row2():
    """Reflejar filtra correctamente imagen 1x2."""
    log(SAMPLE_IMAGES[3])
    check50.run("./testing 2 0").stdout("".join([
        "0 0 255\n", "255 0 0\n"
    ]))

@check50.check(compiles)
def reflect_row3():
    """Reflejar filtra correctamente imagen 1x3."""
    log(SAMPLE_IMAGES[4])
    check50.run("./testing 2 1").stdout("".join([
        "0 0 255\n", "0 255 0\n", "255 0 0\n"
    ]))

@check50.check(compiles)
def reflect_simple():
    """Reflejar filtra correctamente la imagen que es su propia imagen reflejada."""
    log(SAMPLE_IMAGES[0])
    check50.run("./testing 2 2").stdout("".join([
        "255 0 0\n", "255 0 0\n", "255 0 0\n",
        "0 255 0\n", "0 255 0\n", "0 255 0\n",
        "0 0 255\n", "0 0 255\n", "0 0 255\n"
    ]))

@check50.check(compiles)
def reflect3():
    """Reflejar filtra correctamente imagen 3x3."""
    log(SAMPLE_IMAGES[1])
    check50.run("./testing 2 3").stdout("".join([
        "70 80 90\n", "40 50 60\n", "10 20 30\n",
        "130 150 160\n", "120 140 150\n", "110 130 140\n",
        "240 250 255\n", "220 230 240\n", "200 210 220\n"
    ]))

@check50.check(compiles)
def reflect4():
    """Reflejar filtra correctamente imagen 4x4."""
    log(SAMPLE_IMAGES[2])
    check50.run("./testing 2 4").stdout("".join([
        "100 110 120\n", "70 80 90\n", "40 50 60\n", "10 20 30\n",
        "140 160 170\n", "130 150 160\n", "120 140 150\n", "110 130 140\n",
        "245 254 253\n", "225 234 243\n", "205 214 223\n", "195 204 213\n",
        "85 85 85\n", "255 255 255\n", "0 0 0\n", "50 28 90\n"
    ]))

@check50.check(compiles)
def blur_middle():
    """Desenfocar filtra correctamente el píxel medio."""
    log(SAMPLE_IMAGES[1])
    check50.run("./testing 3 0").stdout("127 140 149\n")

@check50.check(compiles)
def blur_edge():
    """Desenfocar filtra correctamente el píxel en el borde."""
    log(SAMPLE_IMAGES[1])
    check50.run("./testing 3 1").stdout("80 95 105\n")

@check50.check(compiles)
def blur_corner():
    """Desenfocar filtra correctamente el píxel en la esquina."""
    log(SAMPLE_IMAGES[1])
    check50.run("./testing 3 2").stdout("70 85 95\n")

@check50.check(compiles)
def blur3():
    """Desenfocar filtra correctamente la imagen 3x3."""
    log(SAMPLE_IMAGES[1])
    check50.run("./testing 3 3").stdout("".join([
        "70 85 95\n", "80 95 105\n", "90 105 115\n",
        "117 130 140\n", "127 140 149\n", "137 150 159\n",
        "163 178 188\n", "170 185 194\n", "178 193 201\n"
    ]))

@check50.check(compiles)
def blur4():
    """Desenfocar filtra correctamente la imagen 4x4."""
    log(SAMPLE_IMAGES[2])
    check50.run("./testing 3 4").stdout("".join([
        "70 85 95\n", "80 95 105\n", "100 115 125\n", "110 125 135\n",
        "113 126 136\n", "123 136 145\n", "142 155 163\n", "152 165 173\n",
        "113 119 136\n", "143 151 164\n", "156 166 171\n", "180 190 194\n",
        "113 112 132\n", "155 156 171\n", "169 174 177\n", "203 207 209\n"
    ]))

@check50.check(compiles)
def edges_middle():
    """Bordes filtra correctamente el píxel medio."""
    log(SAMPLE_IMAGES[5])
    check50.run("./testing 4 0").stdout("210 150 60\n")

@check50.check(compiles)
def edges_edge():
    """Bordes filtra correctamente el píxel en el borde."""
    log(SAMPLE_IMAGES[5])
    check50.run("./testing 4 1").stdout("213 228 255\n")

@check50.check(compiles)
def edges_corner():
    """Bordes filtra correctamente el píxel en la esquina."""
    log(SAMPLE_IMAGES[5])
    check50.run("./testing 4 2").stdout("76 117 255\n")

@check50.check(compiles)
def edges3():
    """Bordes filtra correctamente la imagen 3x3."""
    log(SAMPLE_IMAGES[5])
    check50.run("./testing 4 3").stdout("".join([
        "76 117 255\n", "213 228 255\n", "192 190 255\n",
        "114 102 255\n", "210 150 60\n", "103 108 255\n",
        "114 117 255\n", "200 197 255\n", "210 190 255\n"
    ]))

@check50.check(compiles)
def edges4():
    """Bordes filtra correctamente la imagen 4x4."""
    log(SAMPLE_IMAGES[6])
    check50.run("./testing 4 4").stdout("".join([
        "76 117 255\n", "213 228 255\n", "255 255 255\n", "255 255 255\n",
        "114 102 255\n", "210 150 60\n", "177 171 156\n", "250 247 255\n",
        "161 89 255\n", "126 128 181\n", "114 170 192\n", "247 220 192\n",
        "148 71 156\n", "133 100 121\n", "181 148 212\n", "212 170 255\n"
    ]))

