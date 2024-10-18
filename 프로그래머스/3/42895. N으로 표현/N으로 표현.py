def solution(N, number):
    dp = [set([int(str(N)*i)]) for i in range(1, 9)]
    
    # N 사용 횟수
    for i in range(8):
        for j in range(i):
            # j개
            for num1 in dp[j]:
                # i-j개
                for num2 in dp[i-j-1]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
        # number가 연산한 결과에 있으면 답으로 변환
        if number in dp[i]:
            return i+1
    # 8보다 클경우 -1반환
    return -1