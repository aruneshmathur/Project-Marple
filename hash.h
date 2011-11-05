#ifndef HASHING
#define HASHING
#define B 101
#define M 5463458053 

int integer_mod(int, long long int);
int** generate_hashes(const char*, int);
char* substring(int start, int, char*);
char** generate_k_grams(char*, int);

#endif
