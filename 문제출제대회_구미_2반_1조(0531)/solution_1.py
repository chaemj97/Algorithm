import sys
sys.stdin = open('testcase.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    heights = list(map(int, input().split()))
    # 최고 높이
    Maxh = max(heights)
    # 결과값
    cnt = 0
    for h in range(1, Maxh+1):
        # 높이(h)만큼 있는지 없는지 확인용 flag, 있다(0)고 가정하고 시작
        flag = 0
        for i in range(N):
            if heights[i] < h:
                # 없으면
                if flag % 4 == 0:
                    # 블록 최대 길이 4 고려해서 결과값에 더하기
                    flag = 0
                    cnt += 1
                flag += 1
            else:
                # 있으면
                flag = 0
        if cnt > M:
            print(f'#{tc} FAIL')
            break
    else: print(f'#{tc} {cnt}')

