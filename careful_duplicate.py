def solution(data):
    answer = data

    for i in range(len(answer)):
        temp = answer[i] * answer[i]
        answer[i] = temp

    return answer

def solution(data):
    return [i * i for i in range(data)]