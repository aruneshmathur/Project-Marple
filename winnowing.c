#include "hash.h"
#include "winnowing.h"
#include <stdio.h>
#include <stdlib.h>

void add(struct hash *start, struct hash *node) {
	struct hash *temp = start;
	
	if(temp == NULL) {
		start = node;
		return;
	}
		
	while(temp->next != NULL) {
		start = start->next; 
	}
	
	start->next = node;
	return;
}

struct hash* create_node(int val) {
	struct hash* node = malloc(sizeof(struct hash));
	node->value = val;
	node->next = NULL;

	return node;
}

struct file_winnow_hash* winnowing(struct file_hash* to_winnow, int k) {
	
	int param, i, index;
	long long global_min;

	struct file_winnow_hash* result = malloc(sizeof(struct file_winnow_hash));
	struct hash* new_list = result->list;

	int **list = to_winnow->list;
	
	if(to_winnow->count < k)  param = to_winnow->count; 
	else param = k;

	global_min = M + 1;

	for(i = param - 1; i >= 0; i--) 
		if((*list[i]) < global_min) {
			global_min = (*list[i]);
			index = i;
		}

	add(new_list, create_node(global_min));
	result->count++;
	
	if(to_winnow->count < k)  {
		return result;
	}

	for(i = 1; i < to_winnow->count - k + 1; i++) {
		if(i - index >= 0) {
			
		} else {
			if(*list[k+i] < global_min) {
				global_min = *list[k+i];
				index = i;
			}
			add(new_list, create_node(global_min));
		}
	}

	return result;
}
