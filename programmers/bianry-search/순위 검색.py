from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    # 조회가 O(1)인 dictionary에 기록
    # -를 포함한 모든 조건에 대해 점수 입력
    # 각 배열 정렬
    # 각 조건에 대한 이진탐색으로 문제 해결
    answer = []
    people = defaultdict(list)
    for i in info:
        person = i.split()
        score = int(person.pop())
        people[''.join(person)].append(score)
        
        for j in range(4):
            case = list(combinations(person,j))
            for c in case:
                people[''.join(c)].append(score)
                
    for i in people: people[i].sort()

    for i in query:
        key = i.split()
        score = int(key.pop())
        key = ''.join(key)
        key = key.replace('and','').replace(' ','').replace('-','')
        answer.append(len(people[key]) - bisect_left(people[key],score))
    return answer