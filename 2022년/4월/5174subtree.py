def pre_order(v):
    global descendant
    if v:
        descendant += 1
        pre_order(left[v])
        pre_order(right[v])

# 테스트 케이스 수
T = int(input())
for tc in range(1,T+1):
    # E : 간선의 개수, N을 루트 노드로 하는 서브트리에 속한 노드의 개수 구하기
    E,N = map(int,input().split())
    arr = list(map(int,input().split()))
    # 노드 번호는 1번부터 E+1번까지
    num = E+1

    # 왼쪽 자식, 오른쪽 자식
    left = [0] * (num + 1)
    right = [0] * (num + 1)
    for i in range(0, 2 * E, 2):
        # 왼쪽 자식이 없으면 왼쪽에 넣기
        if left[arr[i]] == 0:
            left[arr[i]] = arr[i + 1]
        else:
            right[arr[i]] = arr[i + 1]

    # 자손의 수
    descendant = 0
    pre_order(N)
    print(f'#{tc} {descendant}')
