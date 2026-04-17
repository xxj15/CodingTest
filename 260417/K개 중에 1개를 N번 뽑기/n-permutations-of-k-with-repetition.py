K, N = map(int, input().split())

# Please write your code here.



arr = []

def pickNum():
    if len(arr) == N:
        print(*arr)
        return 
    
    
    for i in range(1, K+1):
        arr.append(i)
        pickNum()
        arr.pop()

pickNum()
