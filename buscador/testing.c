// testing.c - Small driver used by check50 to call the index functions directly.
// testing.c - Pequeño programa que usa check50 para llamar directamente a las funciones del índice.

#include <stdio.h>
#include <string.h>

#include "indice.h"

#define ROOM 8

int main(int argc, char *argv[])
{
    if (argc != 4)
    {
        printf("Uso: ./testing repositorio palabra max_docs\n");
        return 2;
    }

    if (!load(argv[1]))
    {
        printf("load devolvio false\n");
        return 1;
    }

    // The array is filled with a mark, so anything written past max_docs can be noticed.
    // El arreglo se llena con una marca, para notar si se escribe más allá de max_docs.
    char docs[ROOM][MAX_FILENAME];
    for (int i = 0; i < ROOM; i++)
    {
        strcpy(docs[i], "(sin tocar)");
    }

    unsigned int max_docs = (unsigned int) (argv[3][0] - '0');
    unsigned int n = documents(argv[2], docs, max_docs);

    printf("devolvio %u\n", n);
    for (int i = 0; i < ROOM; i++)
    {
        printf("%i: %s\n", i, docs[i]);
    }
    printf("size %u\n", size());
    printf("unload %s\n", unload() ? "true" : "false");
    return 0;
}
