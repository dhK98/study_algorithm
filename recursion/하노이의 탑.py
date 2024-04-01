def solution(n):
    answer = []
    hanoi(n,1,3,2,answer)
    return answer

def hanoi(n, start, to, mid, answer):
    if n == 1:
        return answer.append([start,to])
    hanoi(n - 1, start, mid, to, answer)
    answer.append([start,to])
    hanoi(n - 1, mid, to, start, answer)

"""
풀이
3개의 원판을 옮기는 과정은 2개의 원판을 옮기는 과정이 출발지와 목적지 중간지점만 다르지 과정은 2번 들어간다
1. n - 1개수의 원판을 start -> mid 로
2. n 개수의 원판은 start -> to로
3. n - 1개수의 원판은 mid에 있으므로 mid -> to
이것을 점화식으로 재귀함수 생성
"""    