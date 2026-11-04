#include <stdio.h>
#include <stdlib.h>

#include "efectosvisuales.h"

#define GRAYSCALE 0
#define POSTERIZE 1
#define REFLECT 2
#define BLUR 3

RGBTRIPLE pixel(int r, int g, int b);
void print_pixel(RGBTRIPLE p);
void print_image(int rows, int cols, RGBTRIPLE img[rows][cols]);

int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        return 1;
    }

    // Determine which test to run
    int function = atoi(argv[1]);
    int test = atoi(argv[2]);

    // 1x2 row
    RGBTRIPLE row2[1][2];
    row2[0][0] = pixel(255, 0, 0);
    row2[0][1] = pixel(0, 0, 255);

    // 1x3 row
    RGBTRIPLE row3[1][3];
    row3[0][0] = pixel(255, 0, 0);
    row3[0][1] = pixel(0, 255, 0);
    row3[0][2] = pixel(0, 0, 255);

    // Grayscale image for grayscale tests
    RGBTRIPLE gimg1[3][3];
    for (int i = 0; i < 3; i++) {
        gimg1[0][i] = pixel(0xff, 0, 0);
        gimg1[1][i] = pixel(0, 0xff, 0);
        gimg1[2][i] = pixel(0, 0, 0xff);
    }

    RGBTRIPLE gimg2[3][3];
    gimg2[0][0] = pixel(10, 20, 30);
    gimg2[0][1] = pixel(40, 50, 60);
    gimg2[0][2] = pixel(70, 80, 90);
    gimg2[1][0] = pixel(110, 130, 140);
    gimg2[1][1] = pixel(120, 140, 150);
    gimg2[1][2] = pixel(130, 150, 160);
    gimg2[2][0] = pixel(200, 210, 220);
    gimg2[2][1] = pixel(220, 230, 240);
    gimg2[2][2] = pixel(240, 250, 255);

    RGBTRIPLE gimg3[4][4];
    gimg3[0][0] = pixel(10, 20, 30);
    gimg3[0][1] = pixel(40, 50, 60);
    gimg3[0][2] = pixel(70, 80, 90);
    gimg3[0][3] = pixel(100, 110, 120);
    gimg3[1][0] = pixel(110, 130, 140);
    gimg3[1][1] = pixel(120, 140, 150);
    gimg3[1][2] = pixel(130, 150, 160);
    gimg3[1][3] = pixel(140, 160, 170);
    gimg3[2][0] = pixel(195, 204, 213);
    gimg3[2][1] = pixel(205, 214, 223);
    gimg3[2][2] = pixel(225, 234, 243);
    gimg3[2][3] = pixel(245, 254, 253);
    gimg3[3][0] = pixel(50, 28, 90);
    gimg3[3][1] = pixel(0, 0, 0);
    gimg3[3][2] = pixel(255, 255, 255);
    gimg3[3][3] = pixel(85, 85, 85);

    // Reflect images
    RGBTRIPLE rimg1[3][3];
    for (int i = 0; i < 3; i++) {
        rimg1[0][i] = pixel(0xff, 0, 0);
        rimg1[1][i] = pixel(0, 0xff, 0);
        rimg1[2][i] = pixel(0, 0, 0xff);
    }

    RGBTRIPLE rimg2[3][3];
    rimg2[0][0] = pixel(10, 20, 30);
    rimg2[0][1] = pixel(40, 50, 60);
    rimg2[0][2] = pixel(70, 80, 90);
    rimg2[1][0] = pixel(110, 130, 140);
    rimg2[1][1] = pixel(120, 140, 150);
    rimg2[1][2] = pixel(130, 150, 160);
    rimg2[2][0] = pixel(200, 210, 220);
    rimg2[2][1] = pixel(220, 230, 240);
    rimg2[2][2] = pixel(240, 250, 255);

    RGBTRIPLE rimg3[4][4];
    rimg3[0][0] = pixel(10, 20, 30);
    rimg3[0][1] = pixel(40, 50, 60);
    rimg3[0][2] = pixel(70, 80, 90);
    rimg3[0][3] = pixel(100, 110, 120);
    rimg3[1][0] = pixel(110, 130, 140);
    rimg3[1][1] = pixel(120, 140, 150);
    rimg3[1][2] = pixel(130, 150, 160);
    rimg3[1][3] = pixel(140, 160, 170);
    rimg3[2][0] = pixel(195, 204, 213);
    rimg3[2][1] = pixel(205, 214, 223);
    rimg3[2][2] = pixel(225, 234, 243);
    rimg3[2][3] = pixel(245, 254, 253);
    rimg3[3][0] = pixel(50, 28, 90);
    rimg3[3][1] = pixel(0, 0, 0);
    rimg3[3][2] = pixel(255, 255, 255);
    rimg3[3][3] = pixel(85, 85, 85);

    // Blur images
    RGBTRIPLE bimg2[3][3];
    bimg2[0][0] = pixel(10, 20, 30);
    bimg2[0][1] = pixel(40, 50, 60);
    bimg2[0][2] = pixel(70, 80, 90);
    bimg2[1][0] = pixel(110, 130, 140);
    bimg2[1][1] = pixel(120, 140, 150);
    bimg2[1][2] = pixel(130, 150, 160);
    bimg2[2][0] = pixel(200, 210, 220);
    bimg2[2][1] = pixel(220, 230, 240);
    bimg2[2][2] = pixel(240, 250, 255);

    RGBTRIPLE bimg3[4][4];
    bimg3[0][0] = pixel(10, 20, 30);
    bimg3[0][1] = pixel(40, 50, 60);
    bimg3[0][2] = pixel(70, 80, 90);
    bimg3[0][3] = pixel(100, 110, 120);
    bimg3[1][0] = pixel(110, 130, 140);
    bimg3[1][1] = pixel(120, 140, 150);
    bimg3[1][2] = pixel(130, 150, 160);
    bimg3[1][3] = pixel(140, 160, 170);
    bimg3[2][0] = pixel(195, 204, 213);
    bimg3[2][1] = pixel(205, 214, 223);
    bimg3[2][2] = pixel(225, 234, 243);
    bimg3[2][3] = pixel(245, 254, 253);
    bimg3[3][0] = pixel(50, 28, 90);
    bimg3[3][1] = pixel(0, 0, 0);
    bimg3[3][2] = pixel(255, 255, 255);
    bimg3[3][3] = pixel(85, 85, 85);

    if (function == GRAYSCALE) {
        switch (test)
        {
            case 0:
            {
                RGBTRIPLE img[1][1];
                img[0][0] = pixel(20, 40, 90);
                grayscale(1, 1, img);
                print_image(1, 1, img);
                break;
            }
            case 1:
            {
                RGBTRIPLE img[1][1];
                img[0][0] = pixel(27, 28, 28);
                grayscale(1, 1, img);
                print_image(1, 1, img);
                break;
            }
            case 2:
            {
                RGBTRIPLE img[1][1];
                img[0][0] = pixel(50, 50, 50);
                grayscale(1, 1, img);
                print_image(1, 1, img);
                break;
            }
            case 3:
            {
                grayscale(3, 3, gimg1);
                print_image(3, 3, gimg1);
                break;
            }
            case 4:
            {
                grayscale(3, 3, gimg2);
                print_image(3, 3, gimg2);
                break;
            }
            case 5:
            {
                grayscale(4, 4, gimg3);
                print_image(4, 4, gimg3);
                break;
            }
        }
    }

    else if (function == POSTERIZE) {
        // Cartoon posterize: 5x5 median (x4), vivid colour, 3 levels, black outlines.
        // Posterize caricatura: mediana 5x5 (x4), color avivado, 3 niveles, contornos negros.
        switch (test)
        {
            case 0:
            {
                // Ejemplo del enunciado: (180, 120, 60) -> (255, 150, 40)
                RGBTRIPLE img[1][1];
                img[0][0] = pixel(180, 120, 60);
                posterize(1, 1, img);
                print_image(1, 1, img);
                break;
            }
            case 1:
            {
                // Un gris se queda gris: (100, 100, 100) -> (150, 150, 150)
                RGBTRIPLE img[1][1];
                img[0][0] = pixel(100, 100, 100);
                posterize(1, 1, img);
                print_image(1, 1, img);
                break;
            }
            case 2:
            {
                // Justo en el límite: 85 ya es nivel medio -> (150, 150, 150)
                RGBTRIPLE img[1][1];
                img[0][0] = pixel(85, 85, 85);
                posterize(1, 1, img);
                print_image(1, 1, img);
                break;
            }
            case 3:
            {
                // Casi blanco: no se desborda -> (255, 255, 255)
                RGBTRIPLE img[1][1];
                img[0][0] = pixel(250, 250, 250);
                posterize(1, 1, img);
                print_image(1, 1, img);
                break;
            }
            case 4:
            {
                // Rojo apagado: avivado queda negativo en verde y azul -> (255, 40, 40)
                RGBTRIPLE img[1][1];
                img[0][0] = pixel(200, 30, 30);
                posterize(1, 1, img);
                print_image(1, 1, img);
                break;
            }
            case 5:
            {
                // 5x5 rojo con un punto azul en el centro: la mediana borra el punto
                RGBTRIPLE img[5][5];
                for (int i = 0; i < 5; i++)
                {
                    for (int j = 0; j < 5; j++)
                    {
                        img[i][j] = pixel(200, 30, 30);
                    }
                }
                img[2][2] = pixel(30, 30, 200);
                posterize(5, 5, img);
                print_image(5, 5, img);
                break;
            }
            case 6:
            {
                // 6x6 mitad roja, mitad azul: debe aparecer un contorno negro entre ambas
                RGBTRIPLE img[6][6];
                for (int i = 0; i < 6; i++)
                {
                    for (int j = 0; j < 6; j++)
                    {
                        img[i][j] = j < 3 ? pixel(200, 30, 30) : pixel(30, 30, 200);
                    }
                }
                posterize(6, 6, img);
                print_image(6, 6, img);
                break;
            }
            case 7:
            {
                // 5x7 con franjas de color: prueba el vecindario 5x5 cerca de los bordes
                RGBTRIPLE img[5][7];
                int r[7] = {230, 210, 40, 30, 120, 250, 90};
                int g[7] = {40, 190, 200, 90, 40, 160, 220};
                int b[7] = {50, 30, 60, 220, 180, 20, 210};
                for (int i = 0; i < 5; i++)
                {
                    for (int j = 0; j < 7; j++)
                    {
                        img[i][j] = pixel(r[(i + j) % 7], g[(i + j) % 7], b[(i + j) % 7]);
                    }
                }
                posterize(5, 7, img);
                print_image(5, 7, img);
                break;
            }
            case 8:
            {
                // 6x6 en diagonal: dos colores separados por una escalera
                RGBTRIPLE img[6][6];
                for (int i = 0; i < 6; i++)
                {
                    for (int j = 0; j < 6; j++)
                    {
                        img[i][j] = j > i ? pixel(250, 180, 30) : pixel(40, 120, 60);
                    }
                }
                posterize(6, 6, img);
                print_image(6, 6, img);
                break;
            }
            case 9:
            {
                // 8x8 con cuatro cuadrantes de color y un píxel suelto en cada uno
                RGBTRIPLE img[8][8];
                for (int i = 0; i < 8; i++)
                {
                    for (int j = 0; j < 8; j++)
                    {
                        if (i < 4 && j < 4)
                        {
                            img[i][j] = pixel(220, 200, 40);
                        }
                        else if (i < 4)
                        {
                            img[i][j] = pixel(60, 170, 70);
                        }
                        else if (j < 4)
                        {
                            img[i][j] = pixel(90, 140, 230);
                        }
                        else
                        {
                            img[i][j] = pixel(240, 240, 235);
                        }
                    }
                }
                img[1][1] = pixel(10, 10, 10);
                img[1][6] = pixel(250, 0, 250);
                img[6][1] = pixel(0, 0, 0);
                img[6][6] = pixel(255, 0, 0);
                posterize(8, 8, img);
                print_image(8, 8, img);
                break;
            }
        }
    }

    else if (function == REFLECT) {
        switch (test)
        {
            case 0:
            {
                reflect(1, 2, row2);
                print_image(1, 2, row2);
                break;
            }
            case 1:
            {
                reflect(1, 3, row3);
                print_image(1, 3, row3);
                break;
            }
            case 2:
            {
                reflect(3, 3, rimg1);
                print_image(3, 3, rimg1);
                break;
            }
            case 3:
            {
                reflect(3, 3, rimg2);
                print_image(3, 3, rimg2);
                break;
            }
            case 4:
            {
                reflect(4, 4, rimg3);
                print_image(4, 4, rimg3);
                break;
            }
        }
    }

    else if (function == BLUR) {
        switch (test)
        {
            case 0:
            {
                blur(3, 3, bimg2);
                print_pixel(bimg2[1][1]);
                break;
            }
            case 1:
            {
                blur(3, 3, bimg2);
                print_pixel(bimg2[0][1]);
                break;
            }
            case 2:
            {
                blur(3, 3, bimg2);
                print_pixel(bimg2[0][0]);
                break;
            }
            case 3:
            {
                blur(3, 3, bimg2);
                print_image(3, 3, bimg2);
                break;
            }
            case 4:
            {
                blur(4, 4, bimg3);
                print_image(4, 4, bimg3);
                break;
            }
        }
    }

}

RGBTRIPLE pixel(int r, int g, int b)
{
    RGBTRIPLE p;
    p.rgbtRed = r;
    p.rgbtGreen = g;
    p.rgbtBlue = b;
    return p;
}

void print_pixel(RGBTRIPLE p)
{
    printf("%i %i %i\n", p.rgbtRed, p.rgbtGreen, p.rgbtBlue);
}

void print_image(int rows, int cols, RGBTRIPLE img[rows][cols])
{
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            print_pixel(img[i][j]);
}
