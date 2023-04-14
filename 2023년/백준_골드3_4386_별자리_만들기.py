'''
    접근법 1
        별과 별 사이 거리 다 구하기!
        거리가 가장 가까운 선부터 연결해보기
            순환이 생기면 연결X
'''
import sys
input = sys.stdin.readline

n = int(input())
star = [list(map(float,input().split())) for _ in range(n)]
p = [i for i in range(n)]

# [d,i,j] : star[i]와 star[j]의 거리가 d
edges = []
for i in range(n):
    for j in range(i+1,n):
        r = abs(star[i][0] - star[j][0])**2
        c = abs(star[i][1] - star[j][1])**2
        d = (r+c)**0.5
        edges.append([d,i,j])

# 부모 찾기
def parent(x):
    if x == p[x]:
        return x
    p[x] = parent(p[x])
    return p[x]
    
# 별 두개 연결
def union(x,y):
    x = parent(x)
    y = parent(y)
    # 더 큰 부모로 연결
    if x > y:
        p[y] = x
    else:
        p[x] = y

edges.sort()
answer = 0
for e in edges:
    d,i,j = e
    # star[i]와 star[j]의 부모 찾기 -> 둘의 부모가 같으면 연결X
    if parent(i) != parent(j):
        # star[i]와 star[j] 연결
        union(i,j)
        answer += d
        
print(round(answer,2))
    
    
