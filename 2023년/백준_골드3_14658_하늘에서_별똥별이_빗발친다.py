'''
    접근법
        최대한 많이 튕겨내기
        모서리에 부딪혀도 튕겨내니 트램펄린의 크기를 (l+1) x (l+1)로 보기
'''
import sys
input = sys.stdin.readline 

# 가로 세로 트램펄린 길이 별똥별수
n, m, l, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(k)]
max_cnt = 0

for i in range(k):
    for j in range(k):
        cnt = 0
        r = arr[i][0]
        c = arr[j][1]
        for x in range(k):
            if r <= arr[x][0] <= r + l and c <= arr[x][1] <= c + l:
                cnt += 1
        max_cnt = max(max_cnt, cnt)

print(k - max_cnt)