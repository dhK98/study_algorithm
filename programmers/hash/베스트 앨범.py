from collections import defaultdict 

def solution(genres, plays):
    answer = []
    # 장르별 재생횟수 기록
    rank = dict()
    # 장르별 음악정보 기록
    info = defaultdict(list)
    # 기록용 반복문
    for i in range(len(plays)):
        kind = genres[i]
        playcount = plays[i]
        index = i
        # 장르별 재생횟수 기록
        rank[kind] = rank.get(kind,0) + playcount
        info[kind].append([index,playcount])
    # 장르별 재생횟수 정렬
    for kind,play in sorted(rank.items(), key = lambda x: x[1], reverse = True):
        info[kind].sort(key = lambda x: x[1], reverse = True)
        if  len(info[kind]) > 0:
            answer.append(info[kind][0][0])
        if len(info[kind]) > 1:
            answer.append(info[kind][1][0])
    return answer

