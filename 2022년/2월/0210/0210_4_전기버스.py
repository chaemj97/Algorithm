import sys
sys.stdin = open('sample_input_4.txt')

# T : 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # K : 최대한 이동할 수 있는 정류장 수
    # N : 종점 정류장 번호
    # M : 충전기가 설치된 정류장 수
    K,N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    cha = [0]*(N+1)
    for i in arr:
        cha[i] += 1
    # 현재 위치
    idx = 0
    # 충전 횟수
    cnt = 0

    # while 현재 위치가 아직 도착점이 아니면:
    while idx < N:
    # 충전소 찾기
    # 1. 갈 수 있는 최대 거리 계산
        if cha[idx+K]:
            idx = idx + K
            cnt += 1
    # 2. 최대거리 부터 뒤로 한 칸씩 가면서 충전소가 있는지 찾음
        else:
            for j in range(1,K):
      # 2-1 만약 충전소를 찾으면 충전하고 충전횟수증가
                if cha[idx+K-j]:
                    idx = idx + K -j
                    cnt += 1
                    break
      # 2-2 만약 현재위치까지 되돌아왔는데 충전소가 없으면, 충전하지 못함 횟수를 0으로 만들고 반복종료
            else:
                cnt = 0
                break

      # 2-3 만약 최대 거리가 도착점보다 멀거나 같으면, 반복종료
        if idx + K >=N:
            idx = N

    # 3. 충전횟수 출력하기
    print(f'#{tc} {cnt}')