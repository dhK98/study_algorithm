# 문제
# 백준이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다. 백준이가 정수를 하나씩 외칠때마다 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다. 
#만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.
# 예를 들어 백준이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면, 동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다. 
# 백준이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 백준이가 외치는 정수의 개수 N이 주어진다. N은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수이다. 
# 그 다음 N줄에 걸쳐서 백준이가 외치는 정수가 차례대로 주어진다. 정수는 -10,000보다 크거나 같고, 10,000보다 작거나 같다.

# 출력
# 한 줄에 하나씩 N줄에 걸쳐 백준이의 동생이 말해야 하는 수를 순서대로 출력한다.

# 풀이
# 두개의 힙을 이용하여 문제를 해결한다.
# left 힙은 최대힙, right는 최대힙을 두어 left의 최소힙이 각 반복문의 정답이 될 수 있도록 한다.
# 두개의 힙은 길이가 같거나 오차 1이 나며 차이가 더 날경우, left의 최대힙을 right로 옮기거나, right의 최소힙을 left로 옮겨야한다.
import sys
import heapq

input = sys.stdin.readline
n = int(input())
left = []
right = []

for i in range(n):
    num = int(input())
    if len(left) == 0 or -left[0] >= num:
        heapq.heappush(left,-num)
    else:
        heapq.heappush(right,num)
    if len(left) > len(right) + 1:
        heapq.heappush(right,-heapq.heappop(left))
    elif len(right)> len(left):
        heapq.heappush(left,-heapq.heappop(right))
    print(-left[0])