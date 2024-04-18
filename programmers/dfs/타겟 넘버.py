def solution(numbers, target):
    answer = 0
    answer = find_target(0,target,0,numbers)
    return answer

def find_target(idx,target,value, numbers):
    if idx == len(numbers):
        if target == value:
            return 1
        else: 
            return 0
    ret = 0
    ret += find_target(idx+1, target, value + numbers[idx], numbers)
    ret += find_target(idx+1, target, value - numbers[idx], numbers)
    return ret
    
    