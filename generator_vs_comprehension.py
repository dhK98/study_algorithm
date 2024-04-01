data = []
# 1 부터 10까지 데이터를 넣는다면 for문을 사용한 기본 형태
for i in range(1,11):
    data.append(i)

# 한줄로 줄이려면 컴프리헨션을 사용
    # tuple, set, dict에서 모두 사용가능
    [i for i in range(1,11)]

    # 조건문을 추가하여 짝수만 뽑고 싶을 때
    [i for i in range(1,11) if i % 2 == 0]

    # 짝수와 5의 배수를 동시에 만족하는 숫자만 필요
    [i for i in range(1,11) if i % 2 == 0 if i % 5 == 0]

# 제너레이터로 바꾸기
    (i for i in range(1,11))    
