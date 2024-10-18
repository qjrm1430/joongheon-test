# input  : 0과 1로 이루어진 문자열 num_str
# output : list
from collections import Counter
import numpy as np
def solution(num_str):
    # x의 모든 0을 제거합니다.
    # x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.
    # 이진 변환 이전	제거할 0의 개수	0 제거 후 길이	이진 변환 결과
    trial = 0
    zero_cnt = 0
    while num_str != '1':
        num_cnt = Counter(num_str)
        zero_cnt += num_cnt['0']
        after_length = num_cnt['1']
        num_str = bin(after_length)[2:]
        trial += 1
        
    answer = [trial, zero_cnt]
    return answer