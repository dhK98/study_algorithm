import re
from itertools import permutations

def solution(expression):
    tokens = re.split(r'([-+*/()])|\s+',expression)
    operators = ['+','-','*']
    answer = 0
    
    for i in map(list,permutations(operators)):
        priority = {o:p for p,o in enumerate(list(i))}
        postfix = toPostFix(tokens,priority)
        answer = max(answer,abs(calc(postfix)))
    return answer  

    
def toPostFix(tokens, priority):
    stack = [] # 연산자 스택
    postfix = [] # 출력 배열
    
    for token in tokens:
        if token.isdigit(): postfix.append(token)
        else:
            if not stack: stack.append(token)
            else:
                while stack:
                    if priority[token] <= priority[stack[-1]]:
                        postfix.append(stack.pop())
                    else:
                        break
                stack.append(token)
            
    while stack:
        postfix.append(stack.pop())
        
    return postfix
    

def calc(tokens):
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            
            if token == '*':
                stack.append(num2 * num1)
            elif token == '+':
                stack.append(num2 + num1)
            elif token == '-':
                stack.append(num2 - num1)
                
    return stack.pop()
            