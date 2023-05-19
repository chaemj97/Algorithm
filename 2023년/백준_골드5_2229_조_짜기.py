'''
    접근법
        j : 0~i-1
        j번째 사람부터 i번째 사람까지 같은 팀 배정하면서 dp 갱신

'''

import sys
input = sys.stdin.readline

# 학생 수
n = int(input())
student = list(map(int,input().split()))

dp = [0]*n
for i in range(1,n):
    for j in range(i-1,-1,-1):
        # j번 학생 ~ i번 학생이 한 팀
        student_ji = student[j:i+1]
        if j == 0:
            j = 1
        # dp[i] : i번 학생까지 최댓값
        # dp[j-1] + max(student_ji)-min(student_ji) : j번 학생 ~ i번 학생이 한 팀일 때 점수 추가
        dp[i] = max(dp[i],dp[j-1]+max(student_ji)-min(student_ji))
print(dp[-1])
