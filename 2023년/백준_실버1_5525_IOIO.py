'''
    접근법 1
        Pn을 세면 50점이 나옴
        아마 시간초과일듯
        
    접근법 2
        'IOI' 연속 개수를 세는게 빠를듯

'''

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()

# 정답
answer = 0
# 'IOI' 개수
cnt = 0
# 시작 위치
i = 0
while i < M-2:
    if S[i:i+3] == 'IOI':
        cnt += 1
        if cnt == N:
           answer += 1
           cnt -= 1
        i += 1
    else:
        cnt = 0
    i += 1

print(answer)