#include <string.h>
#include <stdlib.h>
#include "hash.h"
#include "winnowing.h"

long long integer_mod(int a, long long b) {
	return ((a % b) + b) % b;
}

struct file_hash* generate_hashes(const char* str, int k) {

	int len = strlen(str), count = len - k + 1;
	int i, j = 1;

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
	for(i = 0; i < k; i++) 
	    *ht = integer_mod((*ht * B) + str[i], M);

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

char* substring(int start, int end, char* str) {

	int i = start, len = end - start + 1;

	char* new_str = malloc(len);
	
	while(i < end)  *(new_str++) = *(str+i++);	
	
	*new_str='\0';

	return new_str - len + 1;
}

char** generate_k_grams(char* str, int k) {

	int length = strlen(str);
	int count = length - k + 1;

	if(count <= 0) return NULL;

	int i = 0;

	char** list = malloc(count * sizeof(char*));
	
	while(i < count) {
		list[i] = substring(i, i+k, str);
		i++;
	}
	list[i] = NULL;

	return list;
}
