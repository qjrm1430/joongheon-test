def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = [[0, weight] for weight in truck_weights]
    waiting_truck = []
    while truck_weights or waiting_truck:
        answer += 1

        # 다리를 건너는 중인 트럭들의 상태 업데이트
        for truck in waiting_truck:
            truck[0] += 1

        # 다리를 건넌 트럭들 처리
        waiting_truck = [truck for truck in waiting_truck if truck[0] < bridge_length]

        # 새 트럭을 다리에 올릴 수 있는지 확인
        # if truck_weights and (not waiting_truck or sum(truck[1] for truck in waiting_truck) <= weight):
        if truck_weights and (not waiting_truck or sum(truck[1] for truck in waiting_truck) + truck_weights[0][1] <= weight):
        
            next_truck = truck_weights.pop(0)
            waiting_truck.append(next_truck)
        
    return answer