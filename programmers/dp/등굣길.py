def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    return dfs(0,0,dp,puddles)

def dfs(y,x,dp,puddles):
    row, col = len(dp), len(dp[0])
    path = [[1,0],[0,1]]
    answer = 0
    if [y,x] == [row-1, col-1]: return 1
    if dp[y][x] != 0: return dp[y][x]
    for i in range(2):
        ny = y + path[i][0]
        nx = x + path[i][1]
        if 0 <= ny < row and 0 <= nx < col:
            if [nx + 1, ny + 1] in puddles: continue
            dp[y][x] +=  dfs(ny,nx,dp,puddles)
    return dp[y][x] % 1000000007 

# 완전 탐색에서 중복 방지는 말 그대로 해당 위치를 탐색하지 않게 하는 용도
# 중복방지를 하며 기록했던 데이터를 사용하는 것은 dp의 영역


def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if ([j+1 ,i+1] in puddles) or ((i,j) == (0,0)): continue
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
            
    return dp[-1][-1]