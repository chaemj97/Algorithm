'''
    접근법 1
        사이트 주소와 비밀번호를 딕셔너리의 key, value로 등록
'''

import sys
input = sys.stdin.readline

# 사이트 주소의 수, 비밀번호 찾으려는 사이트 수
N,M = map(int,input().split())

# 사이트
site = {}
for _ in range(N):
    s,p = input().split()
    site[s] = p

# 찾으려는 사이트
for _ in range(M):
    print(site[input().rstrip()])