# https://chaemi720.tistory.com/172

from sys import stdin

# 1부터 N까지 자연수 중 M개 오름차순으로 고르기(중복 허용)
N,M = map(int,stdin.readline().split())

# 직전에 들어간 수, 수열
def check(idx,arr):
    # 수열의 길이가 M인가?
    if len(arr) == M:
        print(*arr)
        return

    # 직전에 넣은 값보다 크거나 같은 값만 수열에 들어갈 수 있음
    for i in range(idx,N+1):
        check(i,arr+[i])

check(1,[])
    
