'''
    접근법 1
        다 입력 받아서 정렬 후 출력하면 '메모리 초과'

        수의 범위가 10,000보다 작거나 같은 자연수이므로 리스트로 숫자 세기

'''

import sys
input = sys.stdin.readline

N = int(input())
# 숫자 오름차순 정렬
num = [0]*10001
for _ in range(N):
    n = int(input())
    num[n] += 1

# 출력
for i,cnt in enumerate(num):
    for j in range(cnt):
        print(i)