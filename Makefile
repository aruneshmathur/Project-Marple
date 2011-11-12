CC = gcc
CFLAGS = -pedantic -Wall -g -std=c99

slce: winnowing.o hash.o main.o list.o
	$(CC) $(CFLAGS) -o slce winnowing.o hash.o list.o main.o

list.o: list.c list.h 
	$(CC) $(CFLAGS) -c list.c

winnowing.o: winnowing.c winnowing.h hash.h
	$(CC) $(CFLAGS) -c winnowing.c

hash.o: hash.c hash.h winnowing.h
	$(CC) $(CFLAGS) -c hash.c

main.o: main.c hash.h winnowing.h list.h
	$(CC) $(CFLAGS) -c main.c

clean: 
	rm *~ *.o ./slce

