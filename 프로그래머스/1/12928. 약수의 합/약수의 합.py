# O(n^5)
# 약수 = n까지 나눴을때 나머지가 0으로 떨어지는 수
# input  : 정수
# output : n의 약수를 모두 더한 값
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    return answer