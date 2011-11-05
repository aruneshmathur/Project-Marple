#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include "hash.h"


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
