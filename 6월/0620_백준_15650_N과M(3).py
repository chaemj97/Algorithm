# https://chaemi720.tistory.com/172

from sys import stdin

# 1부터 N까지 자연수 중 M개 고르기(중복 허용)
N,M = map(int,stdin.readline().split())

# 수열
def check(arr):
    # 수열의 길이가 M인가?
    if len(arr) == M:
        print(*arr)
        return

    # 직전에 넣은 값도 넣을 수 있음
    for i in range(1,N+1):
        check(arr+[i])

check([])
    
