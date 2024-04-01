def solution(s):
    answer = list(s)
    idx = -1
    for i in range(len(answer)):
        if answer[i] == ' ':
            idx = -1
            continue
        idx += 1
        if idx % 2 == 0:
            answer[i] = answer[i].upper()
        else:
            answer[i] = answer[i].lower()
    return ''.join(answer)