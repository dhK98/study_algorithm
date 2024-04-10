def solution(distance, rocks, n):
    answer = 0
    start,end = 0,distance
    rocks.sort()
    
    while start <= end:
        mid = (start + end) // 2
        del_stone = 0
        pre_stone = 0
  
        for i,rock in enumerate(rocks): 
            if rock - pre_stone < mid: del_stone += 1
            else: pre_stone = rock
            
            if del_stone > n: break
            
        if distance - pre_stone < mid: del_stone += 1
            
        if  del_stone > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

    return answer