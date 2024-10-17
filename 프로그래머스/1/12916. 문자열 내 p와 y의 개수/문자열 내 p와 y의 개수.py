# O(n^2)
# input  : 대문자와 소문자가 섞여있는 문자열 s
# output : 
# s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False
# 'p', 'y' 모두 하나도 없는 경우는 항상 True

from collections import Counter

def solution(s):
    # 'p'의 개수와 'y'의 개수 구하기
    p_y_cnt = Counter(s.lower())
    # 비교하기
    return p_y_cnt['p'] == p_y_cnt['y']