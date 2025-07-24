import heapq

def solution(food_times, k):
    
    if sum(food_times) <= k : 
        return -1 
    
    queue = []
    
    for i in range(len(food_times)):
        heapq.heappush(queue, (food_times[i], i+1)) # (음식 번호, 음식 시간)
        
    sum_time = 0 #음식 먹기 위해 사용한 시간 
    finish_food = 0 # 직전에 다 먹은 음식의 시간
    
    length = len(food_times) # 남은 음식 개수 
    
    # 남은 음식 개수 종류 한 번에 없앨 수 있는지 체크 
    while sum_time + ((queue[0][0] - finish_food)*length)<= k :
        now = heapq.heappop(queue)[0]
        sum_time += (now - finish_food) * length 
        length -= 1
        finish_food = now # 이전 음식 시간 재설정 
        
    result = sorted(queue, key = lambda x: x[1]) # 음식 번호를 기준으로 정렬
    ans = result[(k-sum_time)%length][1] 
    
    return ans
