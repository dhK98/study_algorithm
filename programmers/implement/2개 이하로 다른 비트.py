def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0: answer.append(num + 1)
        else:
            num = f'0{str(bin(num)[2:])}'
            result = f"{num[:num.rindex('0')]}10{num[num.rindex('0')+2:]}"
            answer.append(int(result,2))

    return answer