#include "hash.h"
#include "winnowing.h"
#include <stdio.h>
#include <stdlib.h>

struct hash* add(struct hash *start, struct hash *node) {
	
	if(start == NULL) {
		start = node;
		return start;
	}

	struct hash *temp = start;
		
	while(temp->next != NULL) {
		temp = temp->next; 
	}

	temp->next = node;

	return start;
}

struct hash* create_node(long long val) {
	struct hash* node = malloc(sizeof(struct hash));
	node->value = val;
	node->next = NULL;
	return node;
}

struct file_winnow_hash* winnowing(struct file_hash* to_winnow, int k) {
	
	int param, i, index, j;
	long long global_min;

	struct file_winnow_hash* result = malloc(sizeof(struct file_winnow_hash));
	struct hash* new_list;
	new_list = NULL;



	int **list = to_winnow->list;
	
	if(to_winnow->count < k)  param = to_winnow->count; 
	else param = k;

	global_min = M + 1;

	for(i = param - 1; i >= 0; i--) 
		if((*(list[i])) < global_min) {
			global_min = (*(list[i]));
			index = i;
		}

	new_list = add(new_list, create_node(global_min));
	result->count++;
	
	if(to_winnow->count < k)  {
		return result;
	}

	for(i = 1; i < to_winnow->count - k + 1; i++) {
		if(i - index > 0) {
			global_min = M + 1;

			for(j = k + i - 1; j >= i; j--) 
				if((*(list[j])) < global_min) {
					global_min = (*(list[j]));
					index = j;
			}

			new_list = add(new_list, create_node(global_min));			
			result->count++;

		} else {
			if(*list[k + i - 1] < global_min) {
				global_min = *(list[k + i - 1]);
				index = k + i - 1;
				new_list = add(new_list, create_node(global_min));
				result->count++;
			}
		}
	}
	
	result->list = new_list;
	return result;
}
