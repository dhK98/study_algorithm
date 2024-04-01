def solution(s):
    v_cnt = 0
    r_cnt = 0
    while s != "1":
        num, remove_cnt = remove_zero(s)
        r_cnt += remove_cnt
        s = transfort_binary(num)
        v_cnt += 1
    return [v_cnt, r_cnt]

def remove_zero(string):
    one_cnt = 0
    for str in string:
        if str == "1":
            one_cnt += 1
    return (one_cnt, len(string)-one_cnt)

def transfort_binary(num):
    result = []
    while num:
        num, digit = divmod(num,2)
        result.append(str(digit))
    return ''.join(result)