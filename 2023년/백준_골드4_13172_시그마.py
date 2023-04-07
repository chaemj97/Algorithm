'''
    접근법 1
        (Si * Ni^-1)%1000000007 합 구하기
        모듈러에 대해서 몰라도 풀 수 있는 문제였지만 이해가 잘 안되었을 듯
        Ni 곱셈의 역원 구하는게 힘들었는데 python은 pow(n,-1, mod)이라는 내장함수가 있었다...
'''

import sys
input = sys.stdin.readline
# 주사위의 수
M = int(input())
d = 1000000007

# S의 모듈러 곱셈 역원 구하기
def check(n,i):
    if i == 1:
        return n%d
    # i가 짝수
    elif i %2 == 0:
        tmp = check(n,i//2)%d
        return tmp*tmp
    # i가 홀수
    else:
        return n * check(n,i-1)%d

answer = 0

# 주사위
for _ in range(M):
    # Ni면체 주사위,모든 면에 적힌 수를 더한 값이 Si
    # Si/Ni 분수
    N,S = map(int,input().split())
    # (Si * Ni^-1)%d 구하기
    # 페르마 소정리에 의해 (Si*Ni^(d-2))%d 구하기
    answer += S * check(N,d-2)%d

print(answer%d)