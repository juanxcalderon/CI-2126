// Tipos de datos asociados al formato de imagen BMP, basados en las definiciones propias de Microsoft

#include <stdint.h>

/**
* Estos tipos de datos son esencialmente alias para los tipos de datos primitivos de C/C++. 
* Adaptado de http://msdn.microsoft.com/en-us/library/cc230309.aspx.
* Ver https://en.wikipedia.org/wiki/C_data_types#stdint.h para más información sobre stdint.h.
*/
typedef uint8_t  BYTE;
typedef uint32_t DWORD;
typedef int32_t  LONG;
typedef uint16_t WORD;

/**
* La estructura BITMAPFILEHEADER contiene información sobre el tipo, tamaño
* y disposición de un archivo que contiene un DIB [mapa de bits independiente del dispositivo].
* Adaptado de http://msdn.microsoft.com/en-us/library/dd183374(VS.85).aspx.
*/
typedef struct
{
    WORD   bfType;
    DWORD  bfSize;
    WORD   bfReserved1;
    WORD   bfReserved2;
    DWORD  bfOffBits;
} __attribute__((__packed__))
BITMAPFILEHEADER;

/**
* La estructura BITMAPINFOHEADER contiene información sobre las
* dimensiones y el formato de color de un DIB [mapa de bits, independiente del dispositivo].
* Adaptado de http://msdn.microsoft.com/en-us/library/dd183376(VS.85).aspx.
*/
typedef struct
{
    DWORD  biSize;
    LONG   biWidth;
    LONG   biHeight;
    WORD   biPlanes;
    WORD   biBitCount;
    DWORD  biCompression;
    DWORD  biSizeImage;
    LONG   biXPelsPerMeter;
    LONG   biYPelsPerMeter;
    DWORD  biClrUsed;
    DWORD  biClrImportant;
} __attribute__((__packed__))
BITMAPINFOHEADER;

/**
* La estructura RGBTRIPLE describe un color formado de la composición de las intensidades 
* relativas de los tres colores básicos: rojo, verde y azul. 
* Adaptado de http://msdn.microsoft.com/en-us/library/aa922590.aspx.
*/

typedef struct
{
    BYTE  rgbtBlue;
    BYTE  rgbtGreen;
    BYTE  rgbtRed;
} __attribute__((__packed__))
RGBTRIPLE;



