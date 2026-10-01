from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    time = 0
    on_bridge = deque([0]*bridge_length)
    trucks = deque(truck_weights)
    while on_bridge: 
        time += 1
        on_bridge.popleft()
        
        if trucks:
            truck = trucks[0]
            if sum(on_bridge)+truck<=weight:
                on_bridge.append(trucks[0])
                trucks.popleft()
            else:
                on_bridge.append(0)
        
    return time