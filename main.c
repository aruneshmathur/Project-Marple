#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include "hash.h"
#include "winnowing.h"
#include "list.h"


int main() {
	
	struct file_hash* result = generate_hashes("AndreiArshavinisanexcellentplayerIhopehegetshisformbackandperformsagainfortheteam!", 5);
	
	
	if(result) {
		while(*(result->list)) {
			printf("%lld\n", **(result->list));
			*(result->list)++;
		}
	}
	

	/*struct file_winnow_hash	*win = winnowing(result, 4);

	struct hash *list = win->list;

	while(list != NULL) {
		printf("%llu\n", list->value);
		list = list->next;
	}*/

	return 0;
}
