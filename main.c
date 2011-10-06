#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char* substring(int start, int end, char* str) {

	int i = start, len = end-start;

	char* new_str = malloc(len*sizeof (char));
	
	while(i < end) {
		*(new_str++) = *(str+i++);	
	}
	*new_str='\0';

	return (new_str-len);
}

char* generate_k_grams(char* str, int k) {
	int length = strlen(str);
	int count = length-k+1;

	if(count <= 0) return NULL;

	int i = 0;

	char* list[count];
	
	while(i < count) {
		list[i] = substring(i, i+k, str);
		i++;
		printf("%s", list[i]);
	}
}

int main() {
	
	//generate_k_grams("Hello there missy!", 3);

	char* str = substring(0,strlen("Hey I'm here!"),"Hey I'm here!");
	printf("%s\n", str);
	return 0;
}
