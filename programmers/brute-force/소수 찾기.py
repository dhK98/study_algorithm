from itertools import permutations

def solution(numbers):
    answer = 0
    permutations_list = []
    number_list = list(numbers)
    for i in range(1,len(number_list) + 1):
        permutations_list += list(map(''.join,permutations(number_list, i)))

    check_dup = set(list(map(int,permutations_list)))
    
    for pm in check_dup:
        if check_number(int(pm)):
            answer += 1
    return answer

def check_number(number):
    if number < 2: return False
    for i in range(2,number // 2 + 1):
        if number % i == 0:
            return False
    return True