# 생각 블로그
# https://chaemi720.tistory.com/120

# Contact
# 가장 나중에 연락 받게 될 사람 중 번호가 가장 큰 사람

# 테스트 케이스 10개 
for tc in range(1,11):
    # 입력 받는 데이터 길이, 시작점
    length, start = map(int,input().split())

    # 받은 데이터를 연결 형태로 바꾸기
    InputData = list(map(int,input().split()))
    contact = [[0]*101 for _ in range(101)]
    for k in range(0,length,2):
        contact[InputData[k]][InputData[k+1]] = 1

    # 연락 유무(중복 방문 막기), 거리도 표시
    used = [0]*101
    used[start] = 1

    # 이동 시작
    # BFS 선입선출
    q = [start]
    # 결과
    result = start
    while q:
        num= q.pop(0)
        # result 갱신 -> 거리가 멀거나 거리가 같지만 연락받는 사람의 번호가 큰 경우
        if used[result] < used[num] or (used[result] == used[num] and result < num):
            result = num
        for i in range(101):
            # 연결되어있고, 연락 한 적 없다면 -> q에 등록, 거리 표시
            if contact[num][i] and used[i]==0:
                q.append(i)
                used[i] = used[num]+1
    print(f'#{tc} {result}')
