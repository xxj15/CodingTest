# 거꾸로 구구단 
N, K = map(int, input().split())

nums = []

def reverse(number):
    num_list = []
    while number > 0:
        digit = number % 10        # 마지막 자리 꺼내기
        num_list.append(digit)     # 리스트에 넣기
        number = number // 10      # 마지막 자리 버리기
    
    return int("".join(map(str, num_list)))

for i in range(1,K+1):
  num = i * N
  
  nums.append(reverse(num))

print(max(nums))