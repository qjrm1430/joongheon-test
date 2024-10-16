# 배포는 하루에 하나
# 이전 작업이 끝나지 않으면 배포 불가

def solution(progresses, speeds):
    answer = []
    day = 1 
    cnt = 0
    while progresses:
        if progresses[0] + day * speeds[0] >= 100:
            del progresses[0] # 인덱스를 반환해야하는 경우 pop, 아니면 del이 더 빠름
            del speeds[0]
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            day += 1
    answer.append(cnt)       
    return answer