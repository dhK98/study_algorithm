def solution(answers):
    answer = []
    first_p = [1,2,3,4,5]
    second_p = [2,1,2,3,2,4,2,5]
    third_p = [3,3,1,1,2,2,4,4,5,5]
    result = [0] * 3
    
    for i,r in enumerate(answers):
        if answers[i] == first_p[i % len(first_p)]:
            result[0] += 1
        if answers[i] == second_p[i % len(second_p)]:
            result[1] += 1
        if answers[i] == third_p[i % len(third_p)]:
            result[2] += 1
            
    max_value = max(result)
    for index,count in enumerate(result):
        if count == max_value:
            answer.append(index+1)
    return answer

