from collections import deque

def solution(n):
    answer = 0
    lst = deque()
    current_sum = 0
    # 1부터 n까지의 자연수를 순회
    for i in range(1, n + 1):
        lst.append(i)
        current_sum += i
        # 현재 합이 n보다 클 경우, 앞에서부터 값을 제거
        while current_sum > n:
            current_sum -= lst.popleft()
        # 현재 합이 n과 같을 경우, 표현 방법을 하나 추가
        if current_sum == n:
            answer += 1
    return answer
