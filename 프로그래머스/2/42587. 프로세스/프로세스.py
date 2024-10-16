from collections import deque

def solution(priorities, location):
    queue = deque((i, priority) for i, priority in enumerate(priorities))
    answer = 0
    while queue:
        process = queue.popleft()
        if any(process[1] < q[1] for q in queue):
            queue.append(process)
        else:
            answer += 1
            if process[0] == location:
                return answer