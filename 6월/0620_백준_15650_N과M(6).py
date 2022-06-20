from sys import stdin

# N개의 자연수 중 M개 오름차순으로 고르기
N,M = map(int,stdin.readline().split())
num = list(map(int,stdin.readline().split()))

# 사전 순 출력을 위해
num.sort()

# 직전에 넣은 값의 idx+1, 수열, 수열에 들어간 요소 표시
def check(idx, arr, visited):
    print(idx,arr,visited)
    # 수열의 길이가 M인가?
    if len(arr) == M:
        print(*arr)
        return

    # 수열에 들어간 요소표시를 위해 enumerate
    for i,n in enumerate(num[idx:]):
        # 수열에 없다면
        if visited[i] == 0:
            # 수열에 넣기
            visited[i] = 1
            check(i+1, arr+[n],visited)
            # 초기화
            visited[i] = 0

check(0, [], [0]*N)
    
