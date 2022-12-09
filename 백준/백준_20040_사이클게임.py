# 그래프를 트리로 

# 점의 개수, 진행된 차례의 수
n, m = map(int,input().split())

first_cycle_idx = 0
parents = [i for i in range(n)]

def find_parents(i):
    # 부모가 없다면 내가 부모
    if i == parents[i]:
        return i
    # 부모가 있다면
    else:
        j = find_parents(parents[i])
        parents[i] = j
        return j

def union(x,y,idx):
    global first_cycle_idx
    # 부모 찾기
    x = find_parents(x)
    y = find_parents(y)
    # 부모가 다르다면 서로가 부모와 자식 관계로 
    if x != y:
        parents[max(x,y)] = min(x,y) 
    # 부모가 같다면
    else:
        # 첫 사이클이라면 값 갱신
        if first_cycle_idx == 0:
            first_cycle_idx = idx

for i in range(1,m+1):
    # a와 b를 잇기
    a,b = map(int,input().split())
    union(a,b,i)

print(first_cycle_idx)