# Test_504p.py

# 황금미로 = [
#     [1, 4, 4, 2, 2]
#     [1, 3, 3, 0, 5]
#     [1, 2, 4, 3, 0]
#     [3, 3, 0, 4, 2]
#     [1, 3, 4, 5, 3]]

# 메모이제이션 = [[0 for _ in range(5)] for _ in range(5)]

# 열합계 = 황금미로[0][0]
# for i in range(1, 5):
#     열합계 += 황금미로[i][0]
#     메모이제이션[i][0] = 열합계

# 행합계 = 황금미로[0][0]
# for i in range(1, 5):
#     행합계 += 황금미로[0][i]
#     메모이제이션[0][i] = 행합계

# for row in range(1, 5):
#     for col in range(1, 5):
#         if (메모이제이션[row][col-1] > 메모이제이션[row-1][col]):
#             메모이제이션[row][col] = 메모이제이션[row][col-1] + 황금미로[row][col]
#         else:
#             메모이제이션[row][col] = 메모이제이션[row-1][col] + 황금미로[row][col]


def growRich():
    memo = [[0 for _ in range(COL)] for _ in range(ROW)]
    memo[0][0] = goldMaze[0][0]

    rowSum = memo[0][0]
    for i in range(1, ROW):
        rowSum += goldMaze[0][i]
        memo[0][i]=rowSum

    colSum = memo[0][0]
    for i in range(1, COL):
        colSum += goldMaze[i][0]
        memo[i][0] = colSum

    for row in range(1, ROW):
        for col in range(1, COL):
            if (memo[row][col-1] > memo[row-1][col]):
                memo[row][col] = memo[row][col-1] + goldMaze[row][col]
            else:
                memo[row][col] = memo[row-1][col] + goldMaze[row][col]
    
    return memo[ROW-1][COL-1]

ROW, COL = 5, 5
goldMaze= [[1, 4, 4, 2, 2],
           [1, 3, 3, 0, 5],
           [1, 2, 4, 3, 0],
           [3, 3, 0, 4, 2],
           [1, 3, 4, 5, 3]]

macolGold = growRich()
print('황금 미로에서 얻은 최대 황금 개수 -->', macolGold)