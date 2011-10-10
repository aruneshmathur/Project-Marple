#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#define B 101
#define M 5463458053 

int integer_mod(int a, long long int b) {
	return ((a % b) + b) % b;
}

int** generate_hashes(const char* str, int window_size) {

	int len = strlen(str), count = len - window_size + 1;
	int i, j = 1;

	int* ht = malloc(sizeof(int));
	*ht = 0;

	if(count <= 0) return NULL;
	
	int** list = malloc(count * sizeof(int*));

	//Calculate (B^k) -1
	for(i = 0; i < window_size - 1; i++) {
		j = integer_mod(j * B, M);
	}

	// Calculate the initial hash
	for(i = 0; i < window_size; i++) 
	    *ht = integer_mod((*ht * B) + str[i], M);

	list[0] = ht;

	for(i = 1; i < count; i++) {
		ht = malloc(sizeof(int));
		*ht = integer_mod(*list[i-1] - (str[i-1] * j), M);
		*ht = integer_mod(*ht * B, M);
		*ht = integer_mod(*ht + str[i + window_size - 1], M);
		list[i] = ht;
	}

	list[i] = NULL;
	
	return list;
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

int main() {
	
	/*char** list = generate_k_grams("Hello there madam!", 5);*/
	int** list = generate_hashes("Hello there madam!", 5);
	if(list) {
		while(*list) {
			printf("%d\n", **list);
			*list++;
		}
	}

	return 0;
}
