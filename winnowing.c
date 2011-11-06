#include "hash.h"
#include "winnowing.h"

struct file_winnow_hash* winnowing(struct file_hash* to_winnow, int k) {
	
	int param, i, index;
	long long global_min;

	struct file_winnow_hash* result;
	int **list = to_winnow->list, **new_list;
	
	if(to_winnow->count < k)  param = to_winnow->count; 
	else param = k;

	global_min = M + 1;

	for(i = param - 1; i >= 0; i--) 
		if((*list[i]) < global_min) {
			global_min = (*list[i]);
			index = i;
		}
	

	result = malloc(sizeof(struct file_winnow_hash));
	new_list = result->list;
	
	if(to_winnow->count < k)  {

	}
}
