import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())
farm = [list(map(int,input().split())) for _ in range(n)]

answer = 0

visited = [[False] * m for _ in range(n)]

def in_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < m

def can_go(cur_h,x,y):
    global flag
    if not in_range(x,y): # 범위 밖이라면 False
        return False
    if cur_h < farm[x][y]:
        flag = 1
    if visited[x][y] == True or cur_h != farm[x][y]:
        return False
    return True

def dfs(x,y):
    visited[x][y] = True
    h = farm[x][y]
    dxs,dys = [1,-1,0,0,1,-1,1,-1],[0,0,1,-1,1,-1,-1,1]
    for dx,dy in zip(dxs,dys):
        next_x,next_y =  x + dx , y + dy
        if can_go(h,next_x,next_y):
            dfs(next_x,next_y)

for x in range(n):
    for y in range(m):
        if visited[x][y] == False:
            flag = 0
            dfs(x,y)
            if flag == 0:
                answer += 1

print(answer)


