'''
    접근법
        지울 노드 번호와 관련된 노드들 dfs로 삭제
        
        리프노드 : 삭제되지 않은 노드 중 다른 노드의 부모가 아닌 노드
    
'''
import sys
input = sys.stdin.readline

# 노드의 개수
n = int(input())
# 각 노드의 부모노드
parent = list(map(int,input().split()))

# 지울 노드 번호
d = int(input())

def delete_tree(d):
    # d번 노드 삭제
    parent[d] = -100
    # d번 노드의 자식들도 삭제
    for i in range(n):
        if parent[i] == d:
            delete_tree(i)

delete_tree(d)

# 남아있는 리프노드 수
# 리프노드 : 다른 노드의 부모이면 안된다.
answer = 0
for i in range(n):
    if parent[i] != -100 and i not in parent:
        answer += 1 
print(answer)