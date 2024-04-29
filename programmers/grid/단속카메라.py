def solution(routes):
    answer = 0
    stack = []
    routes.sort(key = lambda x: ( x[1],x[0]), reverse = True)
    print(routes)
    while routes:
        start,end = routes.pop()
        answer += 1
        while routes and end >= routes[-1][0]:
            routes.pop()
    return answer