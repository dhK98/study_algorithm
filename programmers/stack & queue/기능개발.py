import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    info = deque([math.ceil((100-progresses[i]) / speeds[i]) for i in range(len(progresses))])
    while info:
        last = info.popleft()
        count = 1
        while info and last >= info[0]:
            info.popleft()
            count += 1
        answer.append(count)
    return answer

