from collections import deque

def solution(n, computers):
    answer = 0
    visit = [False for _ in range(n)]
    for i in range(len(computers)):
        if not visit[i]:
            answer += 1
            visit[i] = True
            que = deque()
            que.append(i)
            while que:
                node = que.popleft()
                for k in range(len(computers[node])):
                    if node != k and computers[node][k] == 1 and not visit[k]:
                            visit[k] = True
                            que.append(k)
    return answer