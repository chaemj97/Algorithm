# https://chaemi720.tistory.com/172

from sys import stdin

# 1부터 N까지 자연수 중 중복 없이 M개 오름차순으로 고르기
N,M = map(int,stdin.readline().split())

# 직전에 들어간 수+1, 수열, 수열에 들어간 요소 표시
def check(idx,arr,visited):
    # 수열의 길이가 M인가?
    if len(arr) == M:
        print(*arr)
        return

    # 직전에 넣은 값보다 큰 값만 수열에 들어갈 수 있음
    for i in range(idx,N+1):
        # 수열에 없다면
        if visited[i] == 0:
            # 수열에 넣기
            visited[i] = 1
            check(i+1, arr+[i],visited)
            # 초기화
            visited[i] = 0

check(1,[],[0]*(N+1))
    
