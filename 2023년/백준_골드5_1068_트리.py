'''
    접근법
    
'''
import sys
input = sys.stdin.readline

# 노드의 개수
n = int(input())
# 각 노드의 부모노드
parent = list(map(int,input().split()))

# 지울 노드 번호
d = int(input())

