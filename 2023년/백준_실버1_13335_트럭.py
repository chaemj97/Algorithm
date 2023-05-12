'''
    접근법
        예제 1 bridge
        time = 0 -> deque([0, 0])
        time = 1 -> deque([0, 7])
        time = 2 -> deque([7, 0])
        time = 3 -> deque([0, 4])
        time = 4 -> deque([4, 5])
        time = 5 -> deque([5, 0])
        time = 6 -> deque([0, 6]) # 마지막 트럭이 다리에 올라왔다
        # 마지막 트럭이 다리를 다 지나가야 끝남
        time += w
'''
from collections import deque
import sys
input = sys.stdin.readline

# 트럭의 수, 다리의 길이, 다리 최대 하중
n,w,l = map(int,input().split())
# 트럭 무게
arr = list(map(int,input().split()))

# 다리
bridge = deque(([0]*w))

time = 0
# 현재 다리 위 무게
weight = 0
i = 0
while i < n:
    time += 1
    # 다리 맨 앞 내리기
    weight -= bridge.popleft()
    # 트럭이 다리에 올라갈 수 있는가?
    if weight + arr[i] <= l:
        weight += arr[i]
        bridge.append(arr[i])
        i += 1
    # 올라 갈 수 없다.
    else:
        # 다리 맨 뒤 공백 추가
        bridge.append(0)

# 마지막에 다리에 올라간 트럭 다리를 다 지나기
print(time+w)