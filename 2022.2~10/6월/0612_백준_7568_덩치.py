# https://chaemi720.tistory.com/162

# 자신보다 덩치가 큰(키도 크고, 몸무게도 많은) 사람 수 +1 == 덩치 등수

# 전체 사람 수
N = int(input())
people = [list(map(int,input().split())) for _ in range(N)]
result = [1]*N

# 덩치 비교
for i in range(N-1):
    for j in range(i+1,N):
        # i번째 사람이 덩치가 더 큰가?
        if people[i][0] > people[j][0] and people[i][1] > people[j][1]:
            result[j] += 1
        # j번째 사람이 덩치가 더 큰가?
        elif people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            result[i] += 1
print(*result)
