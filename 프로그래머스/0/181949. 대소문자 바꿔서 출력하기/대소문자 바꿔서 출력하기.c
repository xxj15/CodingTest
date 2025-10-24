#include <stdio.h>
#include <ctype.h> 
#define LEN_INPUT 10

int main(void) {
    char s1[LEN_INPUT];
    scanf("%s", s1);
    int count = 0;
    while(s1[count]){
        if isupper(s1[count]){
            s1[count] = tolower(s1[count]);
        }
        else{
            s1[count]= toupper(s1[count]);
        }
        count ++;
    }
    printf("%s", s1);
    
    return 0;
}
