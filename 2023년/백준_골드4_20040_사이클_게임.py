'''
    접근법
        그래프 부모 찾기 : find_parent(x)
'''
import sys
input = sys.stdin.readline

# 점의 개수, 차례의 수
n,m = map(int,input().split())

# 사이클 확인 위한 부모 노드
parent = [i for i in range(n)]

def find_parent(x):
    if parent[x] == x:
        return x
    else:
        new_parent = find_parent(parent[x])
        parent[x] = new_parent
        return new_parent

answer = 0
for i in range(1,m+1):
    # a와 b 잇기
    a,b = map(int,input().split())
    # 각각 부모 찾기
    a = find_parent(a)
    b = find_parent(b)
    
    # 둘의 부모가 같으면 사이클 완성
    if a == b:
        answer = i
        break
    # 둘의 부모가 다르면 연결
    else:
        if a > b:
            parent[a] = b
        else:
            parent[b] = a

print(answer)