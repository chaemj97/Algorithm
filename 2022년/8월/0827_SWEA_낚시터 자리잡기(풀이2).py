from itertools import permutations

# 왼쪽으로 자리 잡은 함수
def left(entry,dist):
    global grid, cnt
    
    # 낚시터 범위내이고 빈자리라면
    if entry-dist > 0 and not grid[entry-dist]:
        grid[entry-dist] = dist + 1
        cnt += 1

# 오른쪽으로 자리 잡은 함수
def right(entry,dist):
    global grid, cnt

    # 낚시터 범위내이고 빈자리라면
    if entry+dist <= N and not grid[entry+dist]:
        grid[entry+dist] = dist + 1
        cnt += 1


# 1. 입력
T = int(input())
for t in range(1,T+1):
    N = int(input())
    # 출입구 위치, 낚시꾼 수
    info = [list(map(int,input().split())) for _ in range(3)]

    answer = float('inf')
    ways = [[left,right],[right,left]]

    # 2. 어느 출입문을 먼저 열지 결저
    for turn in permutations(range(3),3):
        # 3. 왼쪽, 오른쪽 중 어떤 방향을 우선시할지 결정
        for way in range(2):
            def1,def2 = ways[way]

            # 4. 낚시꾼 자리 배치
            grid = [0 for _ in range(N+1)]

            for i in turn:
                entry,fisher = info[i]
                
                # 출입구 위치가 비어있는지 파악
                # cnt : entry에서 출발해서 자리잡은 낚시꾼 수
                if grid[entry]:
                    cnt = 0
                else:
                    grid[entry] = 1
                    cnt = 1

                # 낚시꾼들이 모두 자리를 잡을 때까지 반복
                dist = 1
                while cnt < fisher:
                    def1(entry,dist)

                    if cnt == fisher:
                        break
                    
                    def2(entry,dist)

                    dist += 1

            answer = min(answer,sum(grid))
    
    print(f'#{t} {answer}')