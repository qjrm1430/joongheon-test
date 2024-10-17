# input  : 자연수 n
# output : 각 자리 숫자를 원소로 가지는 배열

def solution(n):
    
    return list(map(int, reversed(str(n))))