import sys
input= sys.stdin.readline

str1=list(input().strip())
n = int(input())
str2 = []

for i in range (n):
    cmd = input().strip().split()
    if cmd[0] == 'L':
        if len(str1)>0:
            str2.append(str1.pop())
    elif cmd[0]=='D':
        if len(str2)>0:
            str1.append(str2.pop())
    elif cmd[0]=='B':
        if len(str1)>0:
            str1.pop()
    else : 
        str1.append(cmd[1])

print(''.join(str1 + str2[::-1]))
