#무지의 먹방 라이브 
# https://school.programmers.co.kr/learn/courses/30/lessons/42891?language=python3

# 반복문으로 구현시 효율성 테스트에서 실패 
def solution(food_times, k):
    n = len(food_times)
    idx = 0  

    for _ in range(k):
        # 아직 남은 음식이 없으면 -1
        if sum(food_times) == 0:
            return -1
        
        # 현재 음식 다 먹었으면 다음으로 넘기기
        while food_times[idx] == 0:
            idx = (idx + 1) % n
        
        # 1초 먹기
        food_times[idx] -= 1
        
        # 다음 음식으로
        idx = (idx + 1) % n

    # k초 후 아직 남은 음식이 없으면 -1
    if sum(food_times) == 0:
        return -1
    
    # k초 후 현재 idx에서 먹을 음식 찾기
    while food_times[idx] == 0:
        idx = (idx + 1) % n
    
    return idx + 1  # 음식 번호는 1부터 시작
