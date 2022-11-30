# https://chaemi720.tistory.com/172

from sys import stdin

N, M = map(int, stdin.readline().split())

# 수열, 수열에 들어간 요소 표시
def check(arr,visited):
    # 수열의 길이가 M인가?
    if len(arr) == M:
        print(*arr)
        return

    for i in range(1,N+1):
        # 수열에 없다면
        if visited[i] == 0:
            # 수열에 넣기
            visited[i] = 1
            check(arr+[i],visited)
            # 초기화
            visited[i] = 0

check([],[0]*(N+1))
    