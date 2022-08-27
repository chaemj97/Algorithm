# 3개의 게이트로 순열을 만들어 완전 탐색
# 낚시꾼 배치 시 가까운 곳부터 채워야 함
# 낚시꾼 마지막 인원 배치 시 같은 거리에 낚시터가 2개 존재한다면 둘 다 고려하기

# 3.
# 낚시꾼들 입장
# num : 게이트 위치 번호, angler : 해당 게이트에서 입장하는 낚시꾼 수, r : 앞에서 몇번째 게이트인가

def entrance_gate(num, angler,r):
    global N
    # ret : 모든 낚시꾼 이동 중 거리
    # ret2 : 마지막 낚시꾼이 왼쪽에 입장하고 동일한 거리의 오른쪽에 입장 가능한 경우 위치 반환을 위한 변수
    # dist : 게이트에서 떨어진 정도 (좌우 절댓값으로 증가 예정)
    # flag : 좌우로 체크할 변수 (-1,1)
    ret = 0
    ret2 = False
    dist = 0
    flag = -1 # 왼쪽 우선
    
    # 입장
    # 모든 낚시꾼이 입장할 때까지
    while angler:
        # x : 게이트에서 가장 가까운 낚시터를 너비우선탐색으로 1칸씩 증가하며 탐색
        x = num + (dist*flag)

        # x가 낚시터 범위내이면서, 빈자리
        if 0 <= x < N and fishing[x] == 0:
            # 어느 게이트에서 온 낚시꾼인지 표시
            fishing[x] = r
            ret += dist + 1
            # 낚시꾼 배치
            angler -= 1

        # 같은 거리만큼 떨어진 오른쪽 확인하기 위해
        flag *= -1
        # 왼쪽 먼저 검사 후, 오른쪽을 검사하고 다시 왼쪽을 검사한 경우는 다음칸을 봐야함
        if flag < 0 and angler != 0:
            dist += 1

        # 마지막 낚시꾼이 왼쪽에 들어간 경우, 오른쪽에 들어갈 수 있는 경우가 있는지 체크 후 해당 위치 반환
        if flag > 0 and angler == 0:
            x2 = num + (dist * flag)
            # 오른쪽 입장 한 경우
            if 0 <= x2 < N and fishing[x2] == 0:
                # x는 기존에 왼쪽에 채워진 마지막 낚시꾼 위치
                # x2는 확인해보아야 할 오른쪽 낚시꾼 위치
                ret2 = [x,x2]
    return ret,ret2

# 2.
# 게이트 입장 순서 정하기
# n : 재귀 횟수, total : 낚시꾼이 이동한 총 거리
def dfs(n,total):
    global result
    # 게이트 3개 모두 확인?
    if n == 3:
        # 최소거리?
        if total < result:
            result = total
        return
    
    for i in range(3):
        # 방문했으면 넘기기
        if used[i]:
            continue
        # 방문 안 했다면 방문 표시
        used[i] = 1
        # i번째 게이트 낚시꾼 입장
        ret,ret2 = entrance_gate(info[i][0],info[i][1],i+1)
        dfs(n+1,total+ret)

        # 마지막 낚시꾼이 왼쪽 입장 & 오른쪽 같은 거리에 빈자리가 있어 확인해야 하는 경우
        if ret2:
            fishing[ret2[0]] = 0
            fishing[ret2[1]] = i+1
            dfs(n+1,total+ret)
            # 되돌리기
            fishing[ret2[0]] = i+1
            fishing[ret2[1]] = 0
            
        # fishing 배열의 해당 낚시꾼 입장 초기화
        for j in range(N):
            if fishing[j] == i+1:
                fishing[j] = 0
        used[i] = 0
    return

# 1.
# 테스트 케이스 수
T = int(input())
for tc in range(1,T+1):
    # 낚시터 자리의 개수
    N = int(input())
    # 낚시터
    fishing = [0]*N

    # 게이트, 낚시꾼 정보
    info = []
    # 게이트 사용 여부
    used = [0]*3
    for _ in range(3):
        # 게이트의 위치, 낚시꾼의 수
        gate, cnt = map(int,input().split())
        # 게이트 번호 1부터 시작, index는 0부터 시작
        info.append([gate-1,cnt])

    # 최소 이동 거리
    result = float('inf')

    # dfs
    dfs(0,0)

    print(f'#{tc} {result}')