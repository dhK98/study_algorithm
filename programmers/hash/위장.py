from collections import defaultdict

def solution(clothes):
    answer = 1
    cloth_info = defaultdict(list)
    for cloth,kind in clothes:
        cloth_info[kind].append(cloth)

    length = cloth_info.keys()
     
    if length == 1:
        return length
        
    for key in cloth_info:
        clothes_list = cloth_info[key]
        answer *= len(clothes_list) + 1
        
    return answer -1
