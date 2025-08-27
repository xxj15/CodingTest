#안테나 - 중간값의 성질 알아야함

n = int(input())
homes = list(map(int, input().split()))
homes.sort()

# if n // 2 == 0: 
#   ans = min(homes[(n-1)//2], homes[(n+1)//2])
# else: 
#   ans = homes[(n-1)//2]

print( homes[(n-1)//2])