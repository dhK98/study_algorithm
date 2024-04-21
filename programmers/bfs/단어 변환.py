from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = [0] * len(words)
    # 한개의 단어를 변환하여 변경됨을 체크
    que = deque()
    que.append([begin,0])
    while que:
        word,cnt = que.popleft()
        if target == word: return cnt
        for i in range(len(words)):
            if not visited[i]:
                if check(word,words[i]):    
                    visited[i] = 1
                    que.append([words[i],cnt+1])
    return 0

def check(word1,word2):
    count = 0
    if len(word1) != len(word2):
        return False
    length = len(word1)
    for i in range(length):
        if word1[i] == word2[i]:
            count += 1
    return True if len(word1) - count == 1 else False