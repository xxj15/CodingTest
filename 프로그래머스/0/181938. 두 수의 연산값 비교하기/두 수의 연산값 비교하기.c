#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


int solution(int a, int b) {
    int answer = 0;
    int digit_b = 1;
    int temp = b;

    while(temp>0){
        digit_b *= 10;
        temp /= 10;
    }
    
    int num1 = a*digit_b + b; 
    int num2 = 2 * a * b;
    
    if (num1 >= num2){
        answer = num1;
    }else{
        answer = num2;
    }
    
    return answer;
}