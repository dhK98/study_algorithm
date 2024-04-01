def solution(line):
    points = []
    n = len(line)
    max_x, max_y = -float('inf'), -float('inf')
    min_x, min_y = float('inf'), float('inf')
    # 1. 정수로 나타낼수 있는 모든 교점을 구한다.
    # 2. 그린다.
    # 3. 최소한으로 만든다
    for i in range(n):
        a,b,e = line[i]
        for j in range(i+1,n):
            c,d,f = line[j]
            if a * d == b * c: continue
            x = ((b * f) - (e * d)) / ((a * d) - (b * c))
            y = ((e * c) - (a * f)) / ((a * d) - (b * c))
                      
            if  x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                
                points.append([x,y])
                
                if max_x < x:
                    max_x = x
                if max_y < y:
                    max_y = y
                if min_x > x:
                    min_x = x
                if min_y > y:
                    min_y = y
    
    width = abs(max_x - min_x) + 1
    height = abs(max_y - min_y) + 1
    
    maps = [["." for _ in range(width)] for _ in range(height)]

    for x,y in points:
        maps[max_y - y][x - min_x] = '*'

    return list(map(''.join, maps))

