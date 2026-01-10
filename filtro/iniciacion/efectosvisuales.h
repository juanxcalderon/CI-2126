#include "bmp.h"

// Convierte una imagen BMP a escala de grises
void grayscale(int height, int width, RGBTRIPLE image[height][width]);

// Convierte una imagen BMP a sepia
void sepia(int height, int width, RGBTRIPLE image[height][width]);

// Refleja una imagen BMP horizontalmente
void reflect(int height, int width, RGBTRIPLE image[height][width]);

// Desenfoca una imagen BMP (Blur)
void blur(int height, int width, RGBTRIPLE image[height][width]);

// Convierte una imagen BMP a su negativo fotográfico
void negative(int height, int width, RGBTRIPLE image[height][width]);