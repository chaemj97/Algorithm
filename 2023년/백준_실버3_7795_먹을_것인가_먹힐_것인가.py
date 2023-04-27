'''
    접근법 1
        이분 탐색으로 B 리스트 내의 a보다 작은 수 개수 구하기

'''
import bisect
import sys
input = sys.stdin.readline

# 테스트 케이스 개수
T = int(input())
for _ in range(T):
    # A의 수, B의 수
    n,m = map(int,input().split())
    A = sorted(map(int,input().split()))
    B = sorted(map(int,input().split()))
    
    answer = 0
    for a in A:
        # B에서 a보다 작은 수 개수 
        l = bisect.bisect_left(B,a)
        answer += l
    print(answer)
    