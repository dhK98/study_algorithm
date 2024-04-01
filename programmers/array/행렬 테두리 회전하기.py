def solution(rows, columns, queries):
    answer = []
    # 1씩 증가하는 행렬
    matrix = [[i * columns + (j + 1) for j in range(columns)] for i in range(rows)]
    for y1, x1, y2, x2 in queries:
        x1 = x1 - 1
        x2 = x2 - 1
        y1 = y1 - 1
        y2 = y2 - 1
        values = []
        for x in range(x1, x2 + 1):
            values.append(matrix[y1][x])
            if x != x1:
                matrix[y1][x] = values[-2]
        # x, y1
        for y in range(y1 + 1, y2 + 1):
            values.append(matrix[y][x2])
            matrix[y][x2] = values[-2]
        # x2, y
        for x in range(x2 - 1, x1 - 1, -1):
            values.append(matrix[y2][x])
            matrix[y2][x] = values[-2]
        # x, y2
        for y in range(y2 - 1, y1, -1):
            values.append(matrix[y][x1])
            matrix[y][x1] = values[-2]
        matrix[y1][x1] = values[-1]

        min_value = min(values)
        answer.append(min_value)      

    return answer