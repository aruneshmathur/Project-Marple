#include "list.h"
#include "winnowing.h"
#include <stdio.h>
#include <stdlib.h>

struct project_file_list* add_project_file(struct project_file_list *start, struct project_file_list *node) {
	
	if(start == NULL) {
		start = node;
		return start;
	}

	struct project_file_list *temp = start;
		
	while(temp->next != NULL) {
		temp = temp->next; 
	}

	temp->next = node;

	return start;
}

struct project_file_list* create_project_file(struct file_winnow_hash* list) {
	struct project_file_list *node = malloc(sizeof(struct project_file_list));
	node->list = list;
	node->next = NULL;
	return node;
}
