#ifndef WINNOWING
#define WINNOWING
#define MIN -1

struct hash {
	int value;
	struct hash* next;
}

struct file_winnow_hash {
	struct hash *list;
	int length;
}

struct hash* create_node(int val);
int** winnowing(int** list, int window_size);

#endif

