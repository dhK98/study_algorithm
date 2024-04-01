def solution(num):
    return calculate_collatz(num,0)

def calculate_collatz(number,cnt):
    if number == 1:
        return cnt
    if cnt > 500:
        return -1
    if number % 2 == 0:
        return calculate_collatz(number // 2, cnt + 1)
    else:
        return calculate_collatz(number * 3 + 1, cnt + 1)
    
    # 반복문으로 연산시
def collatz(num):
    for i in range(500):
        num=num/2 if num%2==0 else num*3+1
        if num==1:
            return i+1
    return -1