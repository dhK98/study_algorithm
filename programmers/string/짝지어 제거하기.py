def solution(s):
    stack = list()

    for str in s:
        if check_duplicate(stack, str):
            stack.pop()
        else:
            stack.append(str)
    return 0 if len(stack) > 0 else 1

def check_duplicate(arr, str):
    if len(arr) > 0:
        if arr[-1] == str:
            return True
        else: return False
    else: return False
            