def solution(n, times):
    answer = float('inf')
    low = 0
    high = max(times) * n
    
    while low <= high:
        mid = (low + high) // 2
        m = check_max_n(times,mid)
        if m >= n:
            answer = min(answer,mid)
            high = mid - 1
        else:
            low = mid + 1
            
    return answer

def check_max_n(times,minute):
    result = 0
    for time in times:
        result += minute // time
    return result