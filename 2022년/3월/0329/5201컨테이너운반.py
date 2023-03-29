# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # N : 컨테이너 수, M : 트럭수
    N,M = map(int,input().split())
    # N개의 화물 무게
    w = list(map(int,input().split()))
    # M개 트럭의 적재 용량
    t = list(map(int,input().split()))

    # 오름차순 정리
    w.sort(reverse=True)
    t.sort(reverse=True)
    # 옮긴 컨테이너
    used = [0]*N
    # 화물 이동 가능 최대량
    max_sum = 0

    for i in range(len(t)):
        for j in range(i,len(w)):
            # 옮긴 적 없고, 트럭 적재용량보다 작은 컨테이너
            if not used[j] and t[i] >= w[j]:
                used[j] = 1
                max_sum += w[j]
                break
    print(f'#{tc} {max_sum}')

'''
# 테스트 케이스 개수
T = int(input())
for tc in range(1, T + 1):
    # N : 컨테이너 수, M : 트럭수
    N, M = map(int, input().split())
    # N개의 화물 무게
    w = list(map(int, input().split()))
    # M개 트럭의 적재 용량
    t = list(map(int, input().split()))

    # 오름차순 정리
    w.sort(reverse=True)
    t.sort(reverse=True)

    # 화물 이동 가능 최대량
    max_sum = 0

    j = -1
    for i in range(M):
        while j < N-1:
            j += 1
            # 옮긴 적 없고, 트럭 적재용량보다 작은 컨테이너
            if t[i] >= w[j]:
                max_sum += w[j]
                break
    print(f'#{tc} {max_sum}')
'''