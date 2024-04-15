from collections import defaultdict

def solution(n, results):
    answer = 0
    # 1. 승패를 기록하 딕셔너리 정의
    win,lose = defaultdict(set), defaultdict(set)
    
    # 2. 주어진 결과에서 승/패 정보 기록
    for winner, loser in results:
        # loser를 이긴 사람들
        win[loser].add(winner)
        # winner에게 패배한 사람들
        lose[winner].add(loser)
    # 3. 특수 조건을 반영
    for i in range(1,n + 1):
        for winner in win[i]:
            # i 에게 이긴사람들 기록에다 i에게 패배한 사람들을 기록을 추가 
            lose[winner].update(lose[i])
        for loser in lose[i]:
            # i 에게 패배한 사람들 기록들을 i에게 이긴사람들 기록에 추가
            win[loser].update(win[i])
    for i in range(1,n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1
    return answer


from collections import defaultdict

def solution(n, results):
    answer = 0
    # 플루이드 워셜
    # 1. 승/패 정보를 담을 그래프를 생성
    total = [[0 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        total[i][i] = 'SELF'   
    
    # 승패 기록
    for result in results:
        total[result[0] - 1][result[1] - 1] = "WINS"
        total[result[1] - 1][result[0] - 1] = "LOSE"
    # 플로이드 워셜 알고리즘 사용
    # 가능한 빈 공간을 모두 채워 넣자?
    for k in range(n):
        for i in range(n):
            for j in range(n):
                #   i j의 경기 결과를 판단하기 전 i 와 k , k 와 j 의 경기를 보고 기록되지 않은 경기를 기록
                if total[i][k] == 'WINS' and total[k][j] == 'WINS': total[i][j] = "WINS"
                elif total[i][k] == "LOSE" and total[k][j] == 'LOSE': total[i][j] = "LOSE"
    for i in total:
        if 0 not in i:
            answer += 1
    return answer