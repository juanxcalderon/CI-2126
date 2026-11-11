// buscador.c
// CI-2126 - Mini Buscador con Indice Invertido
// No modifique este archivo.

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/resource.h>
#include <sys/time.h>

#include "indice.h"

#define DEFAULT_REPOSITORIO "repositorio/grande"
#define MAX_RESULTS 1024

static double calculate(const struct rusage *b, const struct rusage *a);
static char *normalize_query(char *s);

int main(int argc, char *argv[])
{
    if (argc != 2 && argc != 3)
    {
        printf("Uso: ./buscador [repositorio] consultas\n");
        return 1;
    }

    const char *repositorio = (argc == 3) ? argv[1] : DEFAULT_REPOSITORIO;
    const char *queries = (argc == 3) ? argv[2] : argv[1];

    FILE *qfile = fopen(queries, "r");
    if (qfile == NULL)
    {
        printf("No se pudo abrir %s.\n", queries);
        return 1;
    }

    struct rusage before, after;

    getrusage(RUSAGE_SELF, &before);
    bool loaded = load(repositorio);
    getrusage(RUSAGE_SELF, &after);
    double time_load = calculate(&before, &after);

    if (!loaded)
    {
        fclose(qfile);
        printf("No se pudo cargar %s.\n", repositorio);
        return 1;
    }

    printf("RESULTADOS\n\n");

    char line[LENGTH + 128];
    char docs[MAX_RESULTS][MAX_FILENAME];
    unsigned int total_queries = 0;
    double time_contains = 0.0;
    double time_documents = 0.0;

    while (fgets(line, sizeof(line), qfile) != NULL)
    {
        char *word = normalize_query(line);
        if (word[0] == '\0')
        {
            continue;
        }

        total_queries++;
        printf("%s:", word);

        getrusage(RUSAGE_SELF, &before);
        bool present = contains(word);
        getrusage(RUSAGE_SELF, &after);
        time_contains += calculate(&before, &after);

        if (present)
        {
            memset(docs, 0, sizeof(docs));
            getrusage(RUSAGE_SELF, &before);
            unsigned int n = documents(word, docs, MAX_RESULTS);
            getrusage(RUSAGE_SELF, &after);
            time_documents += calculate(&before, &after);

            for (unsigned int i = 0; i < n && i < MAX_RESULTS; i++)
            {
                printf(" %s", docs[i]);
            }
        }

        printf("\n");
    }

    fclose(qfile);

    getrusage(RUSAGE_SELF, &before);
    unsigned int words = size();
    getrusage(RUSAGE_SELF, &after);
    double time_size = calculate(&before, &after);

    getrusage(RUSAGE_SELF, &before);
    bool unloaded = unload();
    getrusage(RUSAGE_SELF, &after);
    double time_unload = calculate(&before, &after);

    if (!unloaded)
    {
        printf("No se pudo descargar el indice.\n");
        return 1;
    }

    printf("\nPALABRAS INDEXADAS:                 %u\n", words);
    printf("CONSULTAS PROCESADAS:               %u\n", total_queries);
    printf("TIEMPO DE EJECUCION DE load:        %.2f\n", time_load);
    printf("TIEMPO DE EJECUCION DE contains:    %.2f\n", time_contains);
    printf("TIEMPO DE EJECUCION DE documents:   %.2f\n", time_documents);
    printf("TIEMPO DE EJECUCION DE size:        %.2f\n", time_size);
    printf("TIEMPO DE EJECUCION DE unload:      %.2f\n", time_unload);
    printf("TIEMPO TOTAL:                       %.2f\n",
           time_load + time_contains + time_documents + time_size + time_unload);

    return 0;
}

static double calculate(const struct rusage *b, const struct rusage *a)
{
    if (b == NULL || a == NULL)
    {
        return 0.0;
    }

    return ((((a->ru_utime.tv_sec * 1000000 + a->ru_utime.tv_usec) -
              (b->ru_utime.tv_sec * 1000000 + b->ru_utime.tv_usec)) +
             ((a->ru_stime.tv_sec * 1000000 + a->ru_stime.tv_usec) -
              (b->ru_stime.tv_sec * 1000000 + b->ru_stime.tv_usec))) / 1000000.0);
}

static char *normalize_query(char *s)
{
    // Keeps only the letters of the query. Accented letters and the letter n with tilde take
    // two chars in the file, and the first one is always 0xC3: both chars are kept as they are.
    // Conserva solo las letras de la consulta. Las letras acentuadas y la enie ocupan dos char
    // en el archivo, y el primero siempre vale 0xC3: ambos char se conservan tal como vienen.
    size_t j = 0;

    for (size_t i = 0; s[i] != '\0'; i++)
    {
        unsigned char c = (unsigned char) s[i];

        if (isalpha(c))
        {
            s[j++] = tolower(c);
        }
        else if (c == 0xC3 && s[i + 1] != '\0' && s[i + 1] != '\n' && s[i + 1] != '\r')
        {
            s[j++] = s[i];
            s[j++] = s[i + 1];
            i++;
        }
        else if (c == '\n' || c == '\r')
        {
            break;
        }
    }

    s[j] = '\0';
    return s;
}
