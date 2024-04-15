# 유니온 파인드 구현
def union(parent, x, y):
    x = find(parent,x)
    y = find(parent,y)
    # 서클이 생기면 그만
    if x == y: return
    # x의 자식노드 y추가
    parent[x] = y
    
def find(parent,x):
    if parent[x] == x: return x
    parent[x] = find(parent,parent[x])
    return parent[x]
    
def solution(n, costs):
    answer = 0
    cnt = 0
    parent = [i for i in range(n)]
    costs = sorted(costs, key = lambda x: x[2])
    for i in range(len(costs)):
        if find(parent, costs[i][0]) != find(parent, costs[i][1]):
            union(parent,costs[i][0],costs[i][1])
            cnt += 1
            answer += costs[i][2] 
        if cnt == n - 1:
            break
    return answer
    

    