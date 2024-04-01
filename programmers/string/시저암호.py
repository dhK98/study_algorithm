def solution(s, n):
    answer = ''
    for char in s:
        if char == ' ': 
            answer += char
            continue
        corr = ord('A') if char.isupper() else ord('a')
        answer += chr((ord(char)-corr+n )% 26 + corr)
    return answer