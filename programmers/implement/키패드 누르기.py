def solution(numbers, hand):
    answer = []
    left = [1,4,7]
    right = [3,6,9]
    coordinate = dict()
    current_left = '*'
    current_right = '#'
    
    i = j = 0
    for k in range(1,10):
        coordinate[k] = [i,j]
        j += 1
        if j % 3 == 0:
            i += 1
            j = j % 3

    coordinate['*'] = [3,0]
    coordinate[0] = [3,1]
    coordinate['#'] = [3,2]
    
    for num in numbers:
        if num in left:
            answer.append('L')
            current_left = num
        elif num in right:
            answer.append('R')
            current_right = num
        else:
            target_x, target_y = coordinate[num]
            # 중간 자리일때
            # 좌표 차이 절대값 계산
           
            currnet_left_x, currnet_left_y  = coordinate[current_left]
            current_right_x, current_right_y  = coordinate[current_right]
           
            # 더 작은 값으로 정답
            r_left = abs(currnet_left_x - target_x) + abs(currnet_left_y - target_y)
            r_right = abs(current_right_x - target_x) + abs(current_right_y - target_y)
            if r_left < r_right:
                answer.append('L')
                current_left = num
            elif r_right < r_left:
                answer.append('R')
                current_right = num
            else:
                if hand == 'right':
                    answer.append('R')
                    current_right = num
                else:
                    answer.append('L')
                    current_left = num
            # 같으면 hand에 따라;
            
    return ''.join(answer)