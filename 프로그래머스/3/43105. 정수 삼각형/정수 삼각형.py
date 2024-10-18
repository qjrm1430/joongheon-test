# input
# 삼각형의 정보가 담긴 배열 triangle
# output 
# 거쳐간 숫자의 최댓값

# triangle[i][j]
def solution(triangle):

    height = len(triangle) - 1

    while height > 0:
        for i in range(height):
            triangle[height-1][i] += max([triangle[height][i], triangle[height][i+1]])
        height -= 1

    answer = triangle[0][0]
    return answer