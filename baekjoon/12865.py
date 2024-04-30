# 문제
# 이 문제는 아주 평범한 배낭에 관한 문제이다.
# 한 달 후면 국가의 부름을 받게 되는 준서는 여행을 가려고 한다. 세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기 때문에, 
# 가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다. 준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 
# 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 
# 아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다. 
# 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.

# 입력
# 첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다. 
# 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다. 입력으로 주어지는 모든 수는 정수이다.

# 출력
# 한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.

# 풀이
# dp 갱신
# 무게에 따른 가치 dp 테이블을 갱신해야함
# 1. 무게가 3 가치가 6인 물건 들어옴 -> 
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)]
#DP표는 0~K+1, 0~N+1로 구성하자 (N=1일 때, DP[i-1][j]가 존재해야 하므로)

for i in range(1,N+1):
    for j in range(1,K+1):
        if j >= bag[i-1][0]:  #"현재최대무게j가 해당물건무게보다 큰 경우
        #표의 윗 셀의 값과 현재물건의V+이전물건의V값의 최댓값을 DP[i][j]에 저장
            dp[i][j] = max(bag[i-1][1]+dp[i-1][j-bag[i-1][0]],dp[i-1][j])
        else:
        	#"현재최대무게j가 해당물건무게보다 작은 경우 (현재 물건을 담을 수 없는 경우)
            dp[i][j] = dp[i-1][j]

print(dp[N][K])  #DP[N][K]가 무조건 정답
        
