CC = clang
CFLAGS = -Wall -Wextra -Werror -std=c11

buscador: buscador.o indice.o
	$(CC) $(CFLAGS) -o buscador buscador.o indice.o

buscador.o: buscador.c indice.h
	$(CC) $(CFLAGS) -c buscador.c

indice.o: indice.c indice.h
	$(CC) $(CFLAGS) -c indice.c

clean:
	rm -f *.o buscador
