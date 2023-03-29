# 이동
def hunt(x,y,dist):
    global next, answer

    # 거리가 최소거리보다 크다면 return
    if dist >= answer:
        return
    
    # 일을 끝냄
    if not next:
        answer = min(answer,dist)
        return

    # 3. 다음으로 이동할 지점들로 이동하여 거리 계산
    temp = next[:]
    for num,nx,ny in temp:
        # 다음 이동 거리
        d = abs(x-nx) + abs(y-ny)

        next.remove((num,nx,ny))
        
        # 몬스터일 경우, 고객을 다음에 이동할 수 있는 위치로 추가
        if num > 0:
            i,j = customer[num]
            next.append((-num,i,j))

        hunt(nx,ny,dist+d)

        # 되돌리기
        next.append((num,nx,ny))
        if num > 0:
            next.remove((-num,i,j))

# 1. 입력
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # 2. 입력을 받으며 몬스터, 고객의 위치 저장
    monster = []
    customer = {}

    for i in range(N):
        row = list(map(int,input().split()))
        for j in range(N):
            # 몬스터?
            if row[j] > 0:
                # 몬스터 번호, 행, 열
                monster.append((row[j],i,j))
            # 고객?
            elif row[j] < 0:
                customer[-row[j]] = (i,j)

    # 다음으로 이동할 지정
    next = monster
    answer = float('inf')

    hunt(0,0,0)

    print(f'#{tc} {answer}')