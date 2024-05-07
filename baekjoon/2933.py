import sys

input = sys.stdin.readline
n,m = map(int,input().split())
board = [list(map(str,input().split())) for _ in range(n)]
k = int(input())
attack = [list(map(int,input().split())) for _ in range(k)]
def throw_stick(board, x,y):
    # board[x][y] = '.'
    pass

for i in range(k):
    x = n - attack[i]
    if (i+1) % 2 != 0:
        # 왼쪽
        for j in range(len(board[x])):
            if board[x][j] == "X":
                throw_stick()    
                break
    else:
        # 오른쪽
        for j in range(len(board[x])-1, -1, -1):
            if board[x][j] == "X":
                throw_stick()    
                break
        pass
