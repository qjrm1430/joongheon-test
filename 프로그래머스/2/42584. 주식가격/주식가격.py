from collections import deque

def solution(prices):
    answer = []
    prices_queue = deque(prices)
    cnt = 0
    # prices_queue만큼 반복
    while prices_queue:
        # 현재 prices_queue 첫 price를 뽑음
        price = prices_queue.popleft()
        # 남아있는 prices_queue만큼 반복
        for after_price in prices_queue:
            cnt += 1
            if price > after_price:
                break
        answer.append(cnt)
        cnt = 0
    return answer