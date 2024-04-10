def solution(stones, k):
    answer = 0
    end = max(stones)
    start = 1
    
    while start <= end:
        mid = (start + end) // 2
        if available(mid, stones, k):
            answer = max(answer, mid)
            start = mid + 1
        else:
            end = mid - 1
    return answer


def available(n, stones, k):
    # 다리를 건널 수 있는 지 판단
    skip = 0
    for stone in stones:
        if stone < n:
            skip += 1
            if skip >= k: return False
        else:
            skip = 0
    return True
