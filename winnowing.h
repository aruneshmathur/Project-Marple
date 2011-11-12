#ifndef WINNOWING
#define WINNOWING
#define MIN -1

struct hash {
	long long value;
	struct hash* next;
};

struct file_winnow_hash {
	struct hash *list;
	char *name;
	int count;
	char *file_name;
	char *project_name;
};

struct file_winnow_hash* winnowing(struct file_hash*, int);

#endif

