'''
    접근법
        1. 도시 연결
            그래프 - 부모가 같으면 연결
        2. 여행 가능한지 확인
            가능하지 않은 경로가 1개라도 나오면 NO
    
'''
import sys
input = sys.stdin.readline

# 도시의 수
n = int(input())
# 여행 계획에 속한 도시의 수
m = int(input())
# 연결 (부모가 같으면 연결된 상태)
parent = [i for i in range(n+1)]

def find_parent(x):
    if x == parent[x]:
        return x
    else:
        new_parent = find_parent(parent[x])
        parent[x] = new_parent
        return new_parent
    
# i번 도시 j번 도시 연결
def union(i,j):
    i = find_parent(i)
    j = find_parent(j)
    
    # 이미 연결
    if i == j:
        return
    # 연결
    if i < j:
        parent[j] = i
    else:
        parent[i] = j
        
for i in range(1,n+1):
    link = list(map(int,input().split()))
    for j in range(1,n+1):
        # i번 도시와 j번 도시 연결됨
        if link[j-1] == 1:
            # 연결 표시
            union(i,j)

# 여행 계획
travel_plan = list(map(int,input().split()))

answer = 'YES'
for i in range(len(travel_plan)-1):
    # travel_plan[i]에서 travel[i+1]까지 못간다 == 연결이 되어 있지 않다 == 부모가 다르다
    if parent[travel_plan[i]] != parent[travel_plan[i+1]]:
        answer = 'NO'
        break
print(answer)