# 이렇게 풀어보려했는데 왜 안풀리는지 이해를 못하겠음..
def solution(n, edge):
    dp = [float('inf')] * (n + 1)
    dp[0],dp[1] = 0,0
    start = 1
    edge_ex = [[y,x] for x,y in edge]
    edge.extend(edge_ex) 
    edge.sort(key = lambda x: (x[0],x[1]), reverse = True)
    while start < n and edge:
        while edge and start == edge[-1][0]:
            current_node,next_node = edge.pop()
            dp[next_node] = min(dp[current_node] + 1,dp[next_node]) 
        start += 1
    max_value = max(dp)
    return dp.count(max_value)

from collections import deque

def solution(n, edge):
    answer = []
    visit = [False] * (n + 1)
    graph = [[] for _ in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    que = deque()
    que.append(1)
    visit[1] = True
    while que:
        length = len(que)
        answer.append(length)
        for k in range(length):
            current_node = que.popleft()
            for next_node in graph[current_node]:
                if visit[next_node] == False:
                    visit[next_node] = True
                    que.append(next_node)
                
                
    return answer[-1]