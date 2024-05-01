import sys
input = sys.stdin.readline

n = int(input())
info = list(int(input()) for _ in range(n))
if len(info)<=2: # 계단이 2개 이하일땐 그냥 다 더해서 출력
    print(sum(info))
else:
    dp = [0] * 301
    dp[0] = info[0]
    dp[1] = info[0] + info[1]
    dp[2] = max(info[0] + info[2], info[1] + info[2])
    for i in range(3, n):
        score = info[i]
        dp[i] = max(dp[i-2] + score, info[i-1] + score + dp[i-3])

    print(dp[n-1])  # 수정
