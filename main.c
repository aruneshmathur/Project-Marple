#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include "hash.h"


int main() {
	
	/*char** list = generate_k_grams("Hello there madam!", 5);*/
	struct file_hashes* result = generate_hashes("Hello there madam!", 5);
	
	if(result) {
		while(*(result->list)) {
			printf("%d\n", **(result->list));
			*(result->list)++;
		}
	}

	

	return 0;
}
