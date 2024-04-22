from collections import deque

def solution(maps):
    answer = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    n = len(maps)
    m = len(maps[0])
    visit = [[False] * m for _ in range(n)]
    que = deque()
    que.append([0,0])
    visit[0][0] = True
    while que:

        length = len(que)
        for _ in range(length):
            x,y = que.popleft()
            if x == n - 1 and y == m - 1:
                return answer + 1
            for k in range(4):
                nx = dx[k] + x
                ny = dy[k] + y
                if nx >= 0 and ny >= 0 and nx < n and ny < m and maps[nx][ny] == 1:
                    maps[nx][ny] = 0
                    que.append([nx,ny])
        answer += 1 
        
    return -1