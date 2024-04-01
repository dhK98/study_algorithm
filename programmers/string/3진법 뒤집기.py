def radixChange(num, radix):
    if num == 0: return '0' 
    nums = []
    while num:
        num, digit = divmod(num, radix)
        nums.append(str(digit))
    return ''.join(nums)
def solution(n):
    return int(radixChange(n,3),3)


# def solution(n):
#     if n == 1: return 1
#     answer = list()
#     result = 0
#     while n > 2:
#         answer.append(n % 3)
#         n = n // 3
        
#     if n < 3:
#         answer.append(n)
 
#     value = 0
#     while answer:
#         k = answer.pop()
#         #k * 3의 제곱승
#         result += k * value if value != 0 else k
#         if value == 0: value = 1
#         value *= 3
        
        
#     return result