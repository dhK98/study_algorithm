def solution(name):
    answer = 0
    alpha = dict()
    min_move = len(name) -1 
    for i in range(ord('A'),ord('Z')+1):
        alpha[chr(i)] = i - ord('A') + 1  

    name = list(name)
    min_values = [0] * len(name)
    for i, char in enumerate(name):
        min_value = min(alpha[char]-alpha['A'],alpha['Z']-alpha[char]+1)
        answer += min_value
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        min_move = min([min_move, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
        
    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    return answer
