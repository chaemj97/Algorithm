'''
    접근법
        구현
'''

import sys
input = sys.stdin.readline

# 스위치 개수
n = int(input())
switch = [0]+list(map(int,input().split()))
# 학생수
m = int(input())
for _ in range(m):
    # 성별, 학생이 받은 수
    a,b = map(int,input().split())
    # 남자인가?
    if a == 1:
        # 받은 수의 배수 상태 바꾸기
        for j in range(b,n+1,b):
            switch[j] = (switch[j]+1)%2
            
    # 여자인가?
    else:
        # 좌우대칭이 되는 범위까지 상태 바꾸기
        switch[b] = (switch[b]+1)%2
        cnt = 1
        while True:
            # 범위 내
            if b+cnt <= n and b-cnt > 0:
                # 좌우 대칭?
                if switch[b+cnt] == switch[b-cnt]:
                    switch[b+cnt] = (switch[b+cnt]+1)%2
                    switch[b-cnt] = (switch[b-cnt]+1)%2
                    cnt +=1
                else:
                    break
            else:
                break

# 결과 20개씩 출력
for i in range(1,n,20):
    print(*switch[i:i+20])
