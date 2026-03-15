// Declara la funcionalidad del diccionario

#ifndef DICCIONARIO_H
#define DICCIONARIO_H

#include <stdbool.h>

// Longitud máxima de una palabra
// (ej: pneumonoultramicroscopicsilicovolcanoconiosis)
#define LENGTH 45

// Prototipos de funciones
bool check(const char *word);
unsigned int hash(const char *word);
bool load(const char *dictionary);
unsigned int size(void);
bool unload(void);

#endif // DICCIONARIO_H
