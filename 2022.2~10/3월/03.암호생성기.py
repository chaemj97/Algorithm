# 10개의 테스트 케이스
for _ in range(10):
    # 테스트 케이스 번호
    tc = int(input())
    # 8개의 데이터
    arr=list(map(int,input().split()))

    # 마지막이 0이 나올때까지 반복
    while arr[-1] > 0:
        # 사이클 1~5
        for i in range(1,6):
            # 뺀 값을 마지막에 추가하고 원래 값은 삭제
            # 빼서 0보다 작으면 0으로 바꿔서 넣기
            if arr[0]-i > 0:
                arr.append(arr[0]-i)
                arr.pop(0)
            else:
                arr.append(0)
                arr.pop(0)
                break

    print(f'#{tc}',*arr)