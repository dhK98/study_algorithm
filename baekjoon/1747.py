import math
import sys
input = sys.stdin.readline

n = int(input())

def check_num(k):
    # 소수이면서 펠린드롬인지 확인
    if k < 2:
        return False
    for i in range(2,int(math.sqrt(k)+1)):
        if k % i == 0:
            return False
    k = str(k)
    if k[:] != k[::-1]:
        return False
    return True

while not check_num(n):
    n += 1

print(n)


def solutions(n):
    while not check_num(n):
        n += 1
    print(n)

solutions(31)  
solutions(102)  