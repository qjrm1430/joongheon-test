from collections import deque

def solution(priorities, location):
    
    answer = 0
    queue = deque([(v,i) for i,v in enumerate(priorities)])

    while queue:
        item = queue.popleft()
        if queue and max(queue)[0] > item[0]:
            queue.append(item)
        else:
            answer += 1
            if item[1] == location:
                return answer