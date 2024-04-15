def solution(money):
    answer = 0
    # 문제는 모든 경우의 수를 따져봐야한다. -> 현재 최선의 선택지가 누적되었을 때, 최선이 아닐 수도 있다
    # 현재 지점까지의 훔칠수 있는 돈을 한단계 한단계 높여서 구한다.
    # 내 지점에서 훔칠수 있는 돈 + 내지점 -2의 누적값 vs 내지점 -1의 누적값
    dp1 = [0] * len(money)
    dp1[0] = dp1[1] = money[0]
    
    for i in range(2,len(money)-1):
        dp1[i] = max(money[i]+dp1[i-2],dp1[i-1])
        
    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]
    for i in range(2,len(money)):
        dp2[i] = max(money[i]+dp2[i-2],dp2[i-1])
    return max(max(dp1),max(dp2))