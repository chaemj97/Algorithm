'''
    접근법 1
        목표 : A에서 B로 변환하기 위해 필요한 최소한의 명령어 나열
        시간제한 6초이므로 4가지 경우 모두 구현
'''
from collections import deque
import sys
input = sys.stdin.readline

# 테스트 케이스
T = int(input())
for _ in range(T):
    A, B = map(int,input().split())
    
    num = [0]*10000
    num[A] = 1
    que = deque()
    que.append([A,''])
    while que:
        # 현재 수
        cur, dslr = que.popleft()
        # B로 바뀌었는가?
        if cur == B:
            print(dslr)
            break
        
        # 숫자 바꾸기
        # D
        d = (cur*2)%10000
        if num[d] == 0:
            num[d] = 1
            que.append((d,dslr+'D'))
        # S
        if cur == 0:
            s = 9999
        else:
            s = cur - 1
        if num[s] == 0:
            num[s] = 1
            que.append((s,dslr+'S'))
        # L : 1234 -> 2341
        # 234 == 1234%1000
        # 1 == 1234//1000
        # 2341 == 234*10 + 1
        l = (cur%1000)*10 + cur//1000
        if num[l] == 0:
            num[l] = 1
            que.append((l,dslr+'L'))
        # R : 1234 -> 4123
        # 4 == 1234%10
        # 123 == 1234//10
        # 4123 == 4*1000 + 123
        r = (cur%10)*1000 + cur//10
        if num[r] == 0:
            num[r] = 1
            que.append((r,dslr+'R'))
            