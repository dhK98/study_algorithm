def solution(new_id):
    answer = new_id.lower()
    filterd = []
    for char in answer:
        if char.isalpha() or char.isdigit() or char in ["-","_","."]:
            filterd.append(char)
    i = 0
    while i < len(filterd)-1:
        if filterd[i] == '.' and filterd[i+1] == '.':
            filterd.pop(i)
            continue
        i += 1
        
    if filterd and filterd[0] == '.':
        filterd.pop(0)
    if filterd and filterd[-1] == '.':
        filterd.pop(-1)
    if not filterd:
        filterd.append('a')
        
    end_point = 15 if len(filterd) >= 15 else len(filterd)
    filterd = filterd[0:end_point]
    if filterd and filterd[-1] == '.':
        filterd.pop(-1)

    while len(filterd) <= 2:
        filterd.append(filterd[-1])
        
    return ''.join(filterd)