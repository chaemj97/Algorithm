from collections import deque
# 수빈 위치, 동생 위치
N, K = map(int,input().split())

# 거리 문제니깐 que
def gogo(N,K):
    dist = [0] * (10 ** 5 + 1)
    deq = deque([N])
    while deq:
        # 현 위치
        c = deq.popleft()
        # 잡았다?
        if c == K:
            print(dist[K])
            break
        # 잡으로 가자
        for n in [c-1,c+1,c*2]:
            # 범위 내에 있고 그 위치에 간 적이 없어야 함
            if 0 <= n <= 10**5 and not dist[n]:
                # 이동 횟수
                dist[n] = dist[c] + 1
                deq.append(n)

gogo(N,K)
