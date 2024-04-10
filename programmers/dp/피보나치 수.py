import sys
sys.setrecursionlimit(10**8)

def solution(n):
    refer = [0] * 100002
    answer =  fibonachi(n,refer)
    return answer % 1234567


def fibonachi(n,refer):
    if n <= 0: return 0
    if n == 1: return 1
    if refer[n] != 0:
        return refer[n] 
    refer[n] = fibonachi(n-1,refer)  + fibonachi(n-2,refer)
    return refer[n]
 

 # dp 방식으로 최적하하여 해결
def solution(n):
    a,b = 0,1
    for i in range(n):
        a,b = b, a + b
    return a % 1234567