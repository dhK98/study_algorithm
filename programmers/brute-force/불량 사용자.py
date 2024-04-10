import re

def search(idx, visit, userId, answer, banPatterns):
    if idx == len(banPatterns):
        answer.add(visit)
        return
    
    for i in range(len(userId)):
        print(visit,i)
        if (visit & (1 << i)) != 0 or not re.fullmatch(banPatterns[idx], userId[i]):
            continue
        search(idx+1,visit | (1 << i), userId, answer, banPatterns)
        
def solution(user_id, banned_id):
    answer = set()
    ban_patterns = [x.replace('*', '.') for x in banned_id]
    search(0,0,user_id, answer, ban_patterns)
    return len(answer)

# 정규표현식을 이용
from itertools import permutations
import re

def solution(user_id, banned_id):
    banned = ' '.join(banned_id).replace('*','.')
    print(banned)
    answer = set()

    for i in permutations(user_id,len(banned_id)):
        print(banned, ' '.join(i))
        if re.fullmatch(banned, ' '.join(i)):
            answer.add(''.join(sorted(i)))

    return len(answer)