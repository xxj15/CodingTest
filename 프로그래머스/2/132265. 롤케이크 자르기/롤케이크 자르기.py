from collections import Counter 
def solution(topping):
    answer = 0
    left = set()
    right = Counter(topping)
    right_num = len(right)
    
    for i in range(len(topping)):
        t = topping[i]
        left.add(t)
        
        right[t]-=1
        if right[t]==0:
            right_num -=1
        if right_num == len(left):
            answer += 1
            
    
    return answer