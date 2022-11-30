def shuffle(x, arr, cnt):
    global result, n
    # 5번 넘으면 패쓰
    if cnt > 5:
        return

    # x가 N//2보다 작을 때
    if x <= n - 1:
        arr1 = arr[n - x:n]  # 앞 쪽 카드들 중에서 겹쳐지게(퐁당퐁당?) 될 카드
        arr2 = arr[n:n + x]  # 뒷 쪽 카드들 중에서 겹쳐지게 될 카드
        new_arr = arr[:]  # arr 복사
        for i in range(x):
            new_arr[n - x + 2 * i] = arr2.pop(0)  # 겹칠 부분 번갈아서 pop
            new_arr[n - x + 2 * i + 1] = arr1.pop(0)

    # x가 N//2보다 크면
    else:
        arr1 = arr[:2*n-x-1]  # 앞 쪽 카드들 중에서 겹쳐지게 될 카드
        arr2 = arr[x+1:]  # 뒷 쪽 카드들 중에서 겹쳐지게 될 카드
        new_arr = arr[n:2*n] + arr[:n]  # 이 때부터는 뒷쪽 카드가 앞에 오니까 뒤집어서 복사
        for i in range(2*n-x-1):
            new_arr[x-n+1+i*2] = arr1.pop(0)  # 겹칠 부분 번갈아서 pop
            new_arr[x-n + 2 + i*2] = arr2.pop(0)

    # 셔플하고 오름차거나 내림차면 result에 cnt 추가하고 끗, 아니면 for문으로 x=0 빼고 다 넣어서 재귀, cnt + 1
    if new_arr == sorted(new_arr) or new_arr == sorted(new_arr, reverse=True):
        result.append(cnt)
        return
    else:
        for i in range(1, len(arr)):
            shuffle(i, new_arr, cnt + 1)


T = int(input())
for tc in range(1, T+1):
    result = []
    print(f'#{tc} ', end="")
    N = int(input())
    arr = list(map(int, input().split()))
    n = len(arr) // 2

    # 초반에 정렬되어 있으면 0 출력하고 컨티뉴
    if arr == sorted(arr) or arr == sorted(arr, reverse=True):
        print(0)
        continue
    
    # x = 0일 때 카드 순서에 변화 없으므로 x=0, cnt 0으로 시작
    shuffle(0, arr, 0)

    # 횟수 5가 넘으면 패쓰했기에 최솟값 5라면 result에 저장된 값 없음
    if len(result) == 0:
        print(-1)
    else:
        # 저장된 값 중 최솟값 출력
        print(min(result))