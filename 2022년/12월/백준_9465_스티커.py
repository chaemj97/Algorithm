# https://www.acmicpc.net/problem/9465

# 테스트 케이스의 개수
T = int(input())
for tc in range(T):
    # 2 * n개의 스티커
    n = int(input())
    # 선택할 수 있는 스티커
    # 1. 다음 대각선 스티커
    # 2. 다다음 대각선 스티커
    sticker = [[0] + list(map(int,input().split())) for _ in range(2)]
    
    for i in range(2,n+1):
        for j in range(2):
            # 전 대각선에서 넘어왔는가
            # 전전 대각선에서 넘어왔는가
            sticker[j][i] += max(sticker[(j+1)%2][i-1], sticker[(j+1)%2][i-2])
    # 결과
    print(max(sticker[0][n],sticker[1][n]))