# O(n)
# input  : 자연수 n
# output : n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x
def solution(n):
    for x in range(1, n+1):
        if n % x == 1:
            return x