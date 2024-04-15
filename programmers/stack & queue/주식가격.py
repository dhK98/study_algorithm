# 스택을 사용하지 않았을 때 성공 풀이
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

#스택 사용 풀이

def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            past = stack.pop()
            answer[past] = i - past
        stack.append(i)
    for i in stack:
        answer[i] = len(prices) - 1 - i
    return answer

