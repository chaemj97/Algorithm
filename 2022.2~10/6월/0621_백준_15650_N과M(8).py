# https://chaemi720.tistory.com/178

from sys import stdin

# N개의 자연수 중 M개 오름차순으로 고르기(중복 허용)
N,M = map(int,stdin.readline().split())
num = list(map(int,stdin.readline().split()))

# 오름차순 정렬
num.sort()

def check(idx,arr):
    # 수열의 길이가 M인가?
    if len(arr) == M:
        print(*arr)
        return

    for i in num[idx:]:
        check(num.index(i),arr+[i])

check(0,[])