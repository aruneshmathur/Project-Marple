#ifndef LIST
#define LIST
#include "winnowing.h"

struct project_file_list {
	struct file_winnow_hash* list;
	struct project_file_list* next;
};

struct project_file_list* add(struct project_file_list*, struct project_file_list*);
struct project_file_list* create_node(struct file_winnow_hash*);

#endif
