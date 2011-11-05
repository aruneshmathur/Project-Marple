CC = gcc
CFLAGS = -pedantic -Wall -g -std=c99

vic-cipher: hash.o main.o 
	$(CC) $(CFLAGS) -o slce hash.o main.o

hash.o: hash.c hash.h
	$(CC) $(CFLAGS) -c hash.c

main.o: main.c hash.h
	$(CC) $(CFLAGS) -c main.c

