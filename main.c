#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include "hash.h"
#include "winnowing.h"


int main() {
	
	struct file_hash* result = generate_hashes("Hello there madam!", 5);
	
	/*printf("Hashes\n");
	printf("========\n");

	printf("%d**\n", *((result->list)[0]));
	
	if(result) {
		while(*(result->list)) {
			printf("%d\n", **(result->list));
			*(result->list)++;
		}
	}*/
	

	struct file_winnow_hash	*win = winnowing(result, 4);
	struct hash *list = win->list;

	while(list != NULL) {
		printf("%llu\n", list->value);
		list = list->next;
	}

	return 0;
}
