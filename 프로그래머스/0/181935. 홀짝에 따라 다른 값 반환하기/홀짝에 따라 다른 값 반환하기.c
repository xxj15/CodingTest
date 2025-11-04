#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int check(int n){
    int is_odd = 0;
    
    if (n%2 == 1){
        is_odd = 1;
    }else{
        is_odd = 0;
    }
    
    return is_odd;
}

int solution(int n) {
    int answer = 0;
    int start;
    if (check(n) == 1){
        start = 1;
        while(start<=n){
            answer += start;
            start += 2; 
        } 
    }else{
        start = 2;
        while(start<=n){
            answer+= start*start;
            start += 2;
        }
    }
    
    return answer;
}