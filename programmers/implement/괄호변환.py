from collections import deque

def solution(p):
    answer = dfs(p)
    return answer

def check_balanced(string):
    string = deque(string)
    count = 0
    first_str = string.popleft()
    u = []
    u.append(first_str)
    check_per = []
    check_per.append(first_str)
    count += 1 if first_str == '(' else -1
    while count != 0:
        st =  string.popleft()
        if st == '(':
            count += 1
        else:
            count += -1
        u.append(st)
        if check_per[-1] == '(' and st == ")":
            check_per.pop()
        else:
            check_per.append(st)
    is_perfect = False if len(check_per) > 0 else True
    return (''.join(u),''.join(string),is_perfect)


def dfs(p):
    if p == '':
        return ''
    u, v, is_perfect = check_balanced(p)
    if is_perfect:
        return u + dfs(v)
    else:
        v = '('+dfs(v)+')'
        u = u[1:len(u)-1]  # u의 처음과 끝 괄호 제거
        u = u.replace('(', '.')  # '('를 '.'으로 변경
        u = u.replace(')', '(')  # ')'를 '('으로 변경
        u = u.replace('.', ')')  # '.'를 ')'으로 변경

        return v + u
    
