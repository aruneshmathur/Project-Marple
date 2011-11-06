#ifndef HASHING
#define HASHING
#define B 101
#define M 5463458053

struct file_hash {
	int **list;
	int count;
};

int integer_mod(int, long long);
struct file_hash* generate_hashes(const char*, int);
char* substring(int start, int, char*);
char** generate_k_grams(char*, int);

#endif
