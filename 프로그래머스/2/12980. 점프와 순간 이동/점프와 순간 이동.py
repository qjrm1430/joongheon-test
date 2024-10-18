# 한 번에 K 칸을 앞으로 점프
# (현재까지 온 거리) x 2 에 해당하는 위치로 순간이동
# 건전지 사용량을 줄이자.
# 반대로 거슬러 내려가기
# O(n)
# input  : 거리 1 이상 10억 이하의 자연수
# output : 사용해야 하는 건전지 사용량의 최솟값
def solution(n):
    battery = 0
    while n > 0:
        if n % 2 != 0:
            n -= 1
            battery += 1
        else:
            n /= 2
        
    return battery