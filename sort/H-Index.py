# 주어진 수식 그대로 풀면 비효율적
# def solution(citations):
#     answer = 0
#     max_value = max(citations)
#     for i in range(1,max_value):
#         count = 0
#         for c in citations:
#             if c >= i:
#                 count += 1
#         if count >= i:
#             answer = max(answer,i)
#     return answer

def solution(citations):
    citations.sort()
    for idx, citation in enumerate(citations):
        if citation >= len(citations) - idx:
            return len(citations) - idx
    return 0