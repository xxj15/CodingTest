def move(now_x, now_y, dir):
    if dir == 'U':
        nx, ny = now_x, now_y + 1
    elif dir == 'L':
        nx, ny = now_x -1, now_y
    elif dir == 'R':
        nx, ny = now_x + 1, now_y
    else:
        nx, ny = now_x, now_y-1
    return (nx, ny)

def solution(dirs):
    ans = set()
    x, y = 0, 0 

    for d in dirs:
        nx, ny = move(x,y,d)
        if -5<=nx<=5 and -5<=ny<=5:
            ans.add(((x,y), (nx, ny)))
            ans.add(((nx,ny),(x,y)))
            x, y = nx, ny


    return len(ans)//2