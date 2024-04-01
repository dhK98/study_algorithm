def solution(n):
    maps = [[0] * (i+1) for i in range(n)]
    dy = [1,0,-1]
    dx = [0,1,-1]
    x = y = angle = 0
    cnt = 1
    size = (n + 1) * n // 2
    
    while cnt <= size:
        maps[y][x] = cnt
        cnt += 1
        
        nx = x + dx[angle]
        ny = y + dy[angle]
        if 0 <= ny < n and 0 <= nx <= ny and maps[ny][nx] == 0:
            y,x = ny,nx
        else:
            angle = (angle + 1) % 3
            nx = x + dx[angle]
            ny = y + dy[angle]
        
        x,y = nx,ny
        
            
        # 방향 설정
        # cnt ++
        # 벽에 닿을 경우 체크 후 방향 설정
        
    return [i for j in maps for i in j]