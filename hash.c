#include <string.h>
#include<stdio.h>
#include <stdlib.h>
#include "hash.h"
#include "winnowing.h"

long long integer_mod(long long a, long long b) {
	return ((a % b) + b) % b;
}

struct file_hash* generate_hashes(const char* str, int k) {

	int len = strlen(str), count = len - k + 1;
	int i;
	long long j = 1;

	struct file_hash* result = malloc(sizeof(struct file_hash));

	long long* ht = malloc(sizeof(long long));
	*ht = 0;

	if(count <= 0) return NULL;
	
	long long** list = malloc(count * sizeof(long long*));

	/* Calculate (B^k) -1 */
	for(i = 0; i < k - 1; i++) {
		j = integer_mod(j * B, M);
	}

	/* Calculate the initial hash */
	for(i = 0; i < k; i++) {
	    *ht = integer_mod((*ht * B) + str[i], M);
	}

	list[0] = ht;

	for(i = 1; i < count; i++) {
		ht = malloc(sizeof(long long));
		*ht = integer_mod(*list[i-1] - (str[i-1] * j), M);
		*ht = integer_mod(*ht * B, M);
		*ht = integer_mod(*ht + str[i + k - 1], M);
		list[i] = ht;
	}

	list[i] = NULL;

	result->list = list;
	result->count = count;
	
	return result;
}
