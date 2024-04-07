def solution(brown, yellow):
    answer = []
    total_count = brown + yellow
    
    for n in range(3,total_count // 2 + 1):
        if total_count % n != 0:
            continue
        h = total_count // n
        if (h - 2) * (n -2) == yellow:
            return [h,n]
        
    return answer