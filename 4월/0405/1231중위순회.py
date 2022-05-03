def in_order(n):
    global word
    if n <= N:
        # 왼쪽 자식
        in_order(n*2)
        word += arr[n-1][1]
        # 오른쪽 자식
        in_order(n*2+1)

for tc in range(1,11):
    # 트리가 갖는 정점의 총 수
    N = int(input())
    # 정점 번호, 해당 정점 알파벳, 왼쪽 자식, 오른쪽 자식
    arr = [input().split() for _ in range(N)]

    # 단어
    word = ''
    in_order(1)
    print(f'#{tc} {word}')