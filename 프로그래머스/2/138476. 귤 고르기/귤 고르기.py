from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    tang = defaultdict(int)
    for t in tangerine:
        tang[t]+=1
    sort_tang = sorted(tang.items(), key = lambda x : x[1], reverse=True)
    
    for key, value in sort_tang:
        k-=value
        answer+=1
        if k<=0:
            return answer
        
        
    return answer