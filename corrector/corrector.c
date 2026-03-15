/**
 * Implementa un corrector ortográfico.
 */

#include <ctype.h>
#include <stdio.h>
#include <sys/resource.h>
#include <sys/time.h>
#include <unistd.h>

#include "diccionario.h"
#undef calculate
#undef getrusage

// Diccionario predeterminado
#define DICTIONARY "diccionarios/grande"

int main(int argc, char *argv[])
{
    // Verificar el número correcto de argumentos
    if (argc != 2 && argc != 3)
    {
        printf("Uso: ./corrector [diccionario] texto\n");
        return 1;
    }

    // Determinar qué diccionario usar
    char* dictionary = (argc == 3) ? argv[1] : DICTIONARY;

    bool loaded = load(dictionary);

    // Abortar si el diccionario no pudo cargarse
    if (!loaded)
    {
        printf("No se pudo cargar %s.\n", dictionary);
        return 1;
    }

    // Intentar abrir el texto
    char *text = (argc == 3) ? argv[2] : argv[1];
    FILE *fp = fopen(text, "r");
    if (fp == NULL)
    {
        printf("No se pudo abrir %s.\n", text);
        unload();
        return 1;
    }

    // Preparar para reportar errores ortográficos
    printf("PALABRAS MAL ESCRITAS\n\n");

    // Preparar para revisar ortografía
    int index = 0, misspellings = 0, words = 0;
    char word[LENGTH + 1];

    // Revisar cada palabra del texto
    char c;
    while (fread(&c, sizeof(char), 1, fp))
    {
        // Permitir solo caracteres alfabéticos y apóstrofes
        if (isalpha(c) || (c == '\'' && index > 0))
        {
            // Agregar carácter a la palabra
            word[index] = c;
            index++;

            // Ignorar cadenas alfabéticas demasiado largas para ser palabras
            if (index > LENGTH)
            {
                // Consumir el resto de la cadena alfabética
                while (fread(&c, sizeof(char), 1, fp) && isalpha(c));

                // Preparar para la siguiente palabra
                index = 0;
            }
        }

        // Ignorar palabras con números
        else if (isdigit(c))
        {
            // Consumir el resto de la cadena alfanumérica
            while (fread(&c, sizeof(char), 1, fp) && isalnum(c));

            // Preparar para la siguiente palabra
            index = 0;
        }

        // Se encontró una palabra completa
        else if (index > 0)
        {
            // Terminar la palabra actual
            word[index] = '\0';

            // Actualizar contador
            words++;

            // Verificar ortografía de la palabra
            bool misspelled = !check(word);

            // Imprimir la palabra si está mal escrita
            if (misspelled)
            {
                printf("%s\n", word);
                misspellings++;
            }

            // Preparar para la siguiente palabra
            index = 0;
        }
    }

    // Verificar si hubo un error de lectura
    if (ferror(fp))
    {
        fclose(fp);
        printf("Error al leer %s.\n", text);
        unload();
        return 1;
    }

    // Cerrar el texto
    fclose(fp);

    unsigned int n = size();

    bool unloaded = unload();

    // Abortar si el diccionario no pudo descargarse
    if (!unloaded)
    {
        printf("No se pudo descargar %s.\n", dictionary);
        return 1;
    }

    // Reportar estadísticas
    printf("\nPALABRAS MAL ESCRITAS:       %d\n", misspellings);
    printf("PALABRAS EN EL DICCIONARIO:  %d\n", n);
    printf("PALABRAS EN EL TEXTO:        %d\n", words);

    return 0;
}
