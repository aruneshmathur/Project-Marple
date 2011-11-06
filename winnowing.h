#ifndef WINNOWING
#define WINNOWING
#define MIN -1

struct hash {
	int value;
	struct hash* next;
};

struct file_winnow_hash {
	struct hash *list;
	int count;
};

struct hash* create_node(int val);
struct file_winnow_hash* winnowing(struct file_hash*, int);

#endif

