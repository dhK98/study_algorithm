from math import factorial

def solution(n, k):
    numbers = [i for i in range(1,n + 1)]
    answer = []
    k -= 1
    while numbers:
        print(k)
        idx, k = divmod(k,factorial(len(numbers) - 1))
        answer.append(numbers.pop(idx))
    return answer