def solution(triangle):
    case = [[0] * len(triangle[i]) for i in range(len(triangle))]
    case[0][0] = triangle[0][0]
    # index 0: 왼쪽 아래, index 1: 오른쪽 아래
    dx = [1,1]
    dy = [0,1]
    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i])):
            for k in range(2):
                nx = dx[k]+i
                ny = dy[k]+j
                if nx >= 0 and ny >= 0 and nx < len(triangle) and ny < len(triangle[nx]):
                    case[nx][ny] = max(case[nx][ny],triangle[nx][ny] + case[i][j])
    return max(case[len(case)-1])