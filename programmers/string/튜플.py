def solution(s):
    answer = []
    s_list = s.split('},')
    for i in range(len(s_list)):
        s_list[i] = s_list[i].replace('{','')
        s_list[i] = s_list[i].replace('}','')
        s_list[i]  = s_list[i].split(',')
    s_list.sort(key = lambda x: len(x))
    
    for str in s_list:
        for n in str:
            if int(n) not in answer:
                answer.append(int(n))
    return answer 