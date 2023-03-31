'''
    접근법 1
        num 리스트를 set으로 바꾸어 중복 제거 후 정렬

        1. index로 찾으면 하나하나 확인해야 하므로 시간 초과
        2. 딕셔너리로 바꿔서 key로 찾기
'''

import sys
input = sys.stdin.readline

# N개의 좌표
N = int(input())
num = list(map(int,input().split()))
sorted_num = {k:v for v,k in enumerate(sorted(set(num)))}

answer = []
for n in num:
    answer.append(sorted_num[n])

print(*answer)