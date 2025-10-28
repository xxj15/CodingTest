#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* my_string, int k) {
    int len_str = strlen(my_string);
    char* answer = (char*)malloc(len_str * k + 1);
    int n = 0;
    for (int i = 0; i<k; i++){
        for (int j = 0 ; j<len_str; j++){
            
            answer[n++]=my_string[j];
        }
    }
    
    return answer;
}