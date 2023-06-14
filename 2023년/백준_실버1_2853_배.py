'''
    접근법
        배의 첫 등장을 구하기
            첫 등장 후 주기마다 방문 표시
'''
import sys
input = sys.stdin.readline

# 신나는 날의 개수
n = int(input())
ship = [int(input()) for _ in range(n)]
# 마지막 날
last = ship[-1]

# 배가 오는 날
day = [1]

answer = 0
for i in ship[1:]:
    # 이 배의 첫 등장인가?
    if i not in day:
        answer += 1
        # 간격이 i-1인 배 (1일에 오고 i일에 왔으니)
        for j in range(i,last+1,i-1):
            day.append(j)

print(answer)