# input  : 정수 n
# output : 
def solution(n):
    k = list(str(n))
    k.sort(reverse=True)
    
    return int(''.join(k))