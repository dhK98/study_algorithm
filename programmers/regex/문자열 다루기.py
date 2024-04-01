import re

def solution(s):
    answer = True
    result = re.match('^(\d{4}|\d{6})$',s)
    print(result)
    if result == None: answer = False
    return answer