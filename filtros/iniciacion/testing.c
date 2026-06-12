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

    // Image with three rows demonstrating all four posterization levels
    RGBTRIPLE img1[3][3];
    img1[0][0] = pixel(0,   0,   0);
    img1[0][1] = pixel(64,  64,  64);
    img1[0][2] = pixel(128, 128, 128);
    img1[1][0] = pixel(192, 0,   64);
    img1[1][1] = pixel(0,   192, 128);
    img1[1][2] = pixel(64,  0,   192);
    img1[2][0] = pixel(145, 73,  200);
    img1[2][1] = pixel(32,  96,  160);
    img1[2][2] = pixel(100, 170, 210);

    // Image with varying colors (safe range, no overflow)
    RGBTRIPLE img2[3][3];
    img2[0][0] = pixel(10,  20,  30);
    img2[0][1] = pixel(40,  50,  60);
    img2[0][2] = pixel(70,  80,  90);
    img2[1][0] = pixel(110, 130, 140);
    img2[1][1] = pixel(120, 140, 150);
    img2[1][2] = pixel(130, 150, 160);
    img2[2][0] = pixel(160, 170, 180);
    img2[2][1] = pixel(180, 190, 200);
    img2[2][2] = pixel(200, 210, 220);

    // Larger image (safe range, no overflow)
    RGBTRIPLE img3[4][4];
    img3[0][0] = pixel(10,  20,  30);
    img3[0][1] = pixel(40,  50,  60);
    img3[0][2] = pixel(70,  80,  90);
    img3[0][3] = pixel(100, 110, 120);
    img3[1][0] = pixel(110, 130, 140);
    img3[1][1] = pixel(120, 140, 150);
    img3[1][2] = pixel(130, 150, 160);
    img3[1][3] = pixel(140, 160, 170);
    img3[2][0] = pixel(150, 160, 170);
    img3[2][1] = pixel(160, 170, 180);
    img3[2][2] = pixel(180, 190, 200);
    img3[2][3] = pixel(200, 210, 220);
    img3[3][0] = pixel(50,  28,  90);
    img3[3][1] = pixel(0,   0,   0);
    img3[3][2] = pixel(192, 192, 192);
    img3[3][3] = pixel(85,  85,  85);

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
        switch (test)
        {
            case 0:
            {
                // Pixel del ejemplo del enunciado: (145, 73, 200) -> (128, 64, 192)
                RGBTRIPLE img[1][1];
                img[0][0] = pixel(145, 73, 200);
                posterize(1, 1, img);
                print_image(1, 1, img);
                break;
            }
            case 1:
            {
                // Pixel que redondea hacia abajo: (20, 40, 90) -> (0, 64, 64)
                RGBTRIPLE img[1][1];
                img[0][0] = pixel(20, 40, 90);
                posterize(1, 1, img);
                print_image(1, 1, img);
                break;
            }
            case 2:
            {
                // Pixel ya en un nivel exacto: (64, 128, 192) -> (64, 128, 192)
                RGBTRIPLE img[1][1];
                img[0][0] = pixel(64, 128, 192);
                posterize(1, 1, img);
                print_image(1, 1, img);
                break;
            }
            case 3:
            {
                // Imagen 3x3 que demuestra todos los niveles
                posterize(3, 3, img1);
                print_image(3, 3, img1);
                break;
            }
            case 4:
            {
                // Imagen 3x3 con colores variados (rango seguro)
                posterize(3, 3, img2);
                print_image(3, 3, img2);
                break;
            }
            case 5:
            {
                // Imagen 4x4
                posterize(4, 4, img3);
                print_image(4, 4, img3);
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
