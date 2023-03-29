import sys
input = sys.stdin.readline

# 회의 수
N = int(input())

# 시작시간, 끝나는 시간
meeting = []
for _ in range(N):
    s,e = map(int,input().split())
    meeting.append([s,e])
# 빨리 끝나고 일찍 시작하는 순
meeting.sort(key=lambda x:(x[1],x[0]))

answer = 1
end_time = meeting[0][1]
for i in range(1,N):
    # 시작시간이 이전회의 종료시간 이후여야함
    if meeting[i][0] >= end_time:
        end_time = meeting[i][1]
        answer += 1
print(answer)

