# https://chaemi720.tistory.com/141

# 멜로디에 포함되어 있는 음의 수, 한 줄에 있는 프렛의 수
N, P = map(int,input().split())
# [줄의 번호, 그 줄에서 눌러야 하는 프렛의 번호], 행의 순서대로 연수
melody = [list(map(int,input().split())) for _ in range(N)]

finger = [[] for _ in range(7)]
finger[melody[0][0]] += [melody[0][1]]
# 손가락 움직인 횟수, 일단 첫음을 누르고 시작해보자
cnt = 1

# 음의 순서대로 기타를 연주해보자
for i in range(1,N):
    while True:
        # 그 기타 줄을 누르지 않고 있거나 그 기타 줄에 눌려진 프렛보다 높은 프렛을 누르려고 하면 -> 누르기만 하면 됨
        if not finger[melody[i][0]] or finger[melody[i][0]][-1] < melody[i][1]:
            cnt += 1
            finger[melody[i][0]] += [melody[i][1]]
            break
        # 그 기타 줄에 눌려진 프렛보다 낮은 프렛을 누르고 싶으면 -> 그 기타줄에 마지막에 추가로 누른 프렛을 손 떼보자
        if finger[melody[i][0]][-1] > melody[i][1]:
            cnt += 1
            finger[melody[i][0]].pop()
        # 이미 그 기타 줄에 마지막으로 누른 프렛을 연주하고 싶으면 -> 그냥 연주 하자
        else:
            break
print(cnt)