#include <stdio.h> 
#include <stdlib.h> 
#define N 256 

int* element_count(char* str) 
{ 
	int* count = (int*)calloc( 
		sizeof(int), N); 
	int i; 
	for (i = 0; *(str + i); i++) 
		count[*(str + i)]++; 
	return count; 
} 

int firstNonRepeat(char* str) 
{ 
	int* count = element_count(str); 
	int index = -1, i; 

	for (i = 0; *(str + i); i++) { 
		if (count[*(str + i)] == 1) { 
			index = i; 
			break; 
		} 
	} 

	free(count); 
	return index; 
} 

int main() 
{ 
	char str[10000]; 
	scanf("%s", str);
	int index = firstNonRepeat(str); 
	if (index == -1) 
		printf("_"); 
	else
		printf("%c", str[index]); 
	getchar(); 
	return 0; 
} 
