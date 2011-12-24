CC = gcc
CFLAGS = -pedantic -Wall -g -std=c99

slce: winnowing.o hash.o main.o 
	$(CC) $(CFLAGS) -o slce winnowing.o hash.o main.o

winnowing.o: winnowing.c winnowing.h hash.h
	$(CC) $(CFLAGS) -c winnowing.c

hash.o: hash.c hash.h winnowing.h
	$(CC) $(CFLAGS) -c hash.c

main.o: main.c hash.h winnowing.h
	$(CC) $(CFLAGS) -c main.c

clean: 
	rm *~ *.o ./slce

