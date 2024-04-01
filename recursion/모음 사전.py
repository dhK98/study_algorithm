# 스스로 푼 방식
def solution(word):
    word_list = ['A','E','I','O','U']
    dup_check = set()
    cnt = 0
    stop = False
    
    def dfs(word,answer,word_list):
        nonlocal cnt
        nonlocal stop
        if ''.join(word) == answer:
            stop = True
            return
        if len(word) == 5:
            return 
        for i in range(len(word_list)):
            word_cp = word.copy()
            word_cp.append(word_list[i])
            if ''.join(word_cp) not in dup_check and not stop:
                cnt += 1
                dup_check.add(''.join(word_cp))
                dfs(word_cp,answer,word_list)
            else:
                return
                
    dfs([],word,word_list)
        
    return cnt

# 정석 풀이 1(재귀)
def find(data, p, step): # 사건을 기록할 배열, 현재 문자열, 현재 문자열 숫자
    if step == 6: return
    if p != '': data.append(p)
    for c in ['A','E','I','O','U']:
        find(data, ''.join([p,c],step+1))
    

def solution(word):
    answer = 0
    data = []
    find(data,'',0)
    # 데이터를 생성 후 해당 데이터의 인덱스를 조회
    for i in range(len(data)):
        if data[i] == word:
            answer = i + 1
            break

    return answer


