def solution(N, number):
    dp = [set() for i in range(9)]
    for i in range(1,9):
        n = int(str(N)*i)
        case = dp[i]
        case.add(n)
        
        for j in range(1,i):
            for k in dp[j]:
                for l in dp[i-j]:
                    case.add(k+l)
                    case.add(k*l)
                    case.add(k-l)
                    if k != 0 and l != 0:
                        case.add(k // l)
        
        if number in case:
            return i
    return -1