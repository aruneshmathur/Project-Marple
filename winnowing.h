#ifndef WINNOWING
#define WINNOWING
#define MIN -1

struct hash {
	
}

struct file_winnow_hash {
	struct hash *list;
	int length;
}

int** winnowing(int** list, int window_size);

#endif

