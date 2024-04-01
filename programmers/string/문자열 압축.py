def solution(s):
    answer = len(s)
    # 압축 가능한 길이만큼 순회 (s // 2)
    for x in range(1,len(s) // 2 + 1):
        # 반복 횟수, 반복된 문자열 기록
        comp_len = 0
        comp = ''
        cnt = 1
        for i in range(0,len(s)+1, x):
            temp = s[i:i + x]
            if comp == temp: cnt += 1
            elif comp != temp:
                comp_len += len(temp)
                if cnt > 1: comp_len += len(str(cnt))
                cnt = 1
                comp = temp
                
        answer = min(answer, comp_len)
    return answer