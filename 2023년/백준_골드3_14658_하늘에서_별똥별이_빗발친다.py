'''
    접근법
        최대한 많이 튕겨내기
        모서리에 부딪혀도 튕겨내니 트램펄린의 크기를 (l+1) x (l+1)로 보기
'''
import sys
input = sys.stdin.readline

n,m,l,k = map(int,input().split())

star = [list(map(int,input().split())) for _ in range(k)]

for a in range(k):
    for b in range(k):
        cnt = 0
        for c in range(k):
            pass