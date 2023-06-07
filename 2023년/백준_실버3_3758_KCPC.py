'''
    접근법
        [-최종 점수, 제출 횟수, 마지막 제출 시간, idx]
    
'''

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # 팀의 개수, 문제 개수, 내 팀 id, 로그 개수
    n,k,t,m = map(int,input().split())
    
    score = [[0]*(k+1) for _ in range(n+1)]
    cnt = [0]*(n+1)
    last = [0]*(n+1)
    # 풀이 로그
    for l in range(m):
        # 팀 id, 문제 번호, 점수
        i,j,s = map(int,input().split())
        score[i][j] = max(score[i][j],s)        
        cnt[i] += 1
        last[i] = l

    # [-최종 점수, 제출 횟수, 마지막 제출 시간, idx]
    team = [[0,0,0,idx] for idx in range(n+1)]
    for a in range(1,n+1):
        # -최종 점수
        team[a][0] = -sum(score[a])
        # 풀이 제출 횟수
        team[a][1] = cnt[a]
        # 마지막 제출 시간
        team[a][2] = last[a]
    
    answer = 1
    team.sort()
    for i in range(n):
        if team[i][3] == t:
            print(answer)
            break
        answer += 1