def post_odrer(v):
    if v:
        post_odrer(left[v])
        post_odrer(right[v])
        if tree[v] == '+':
            tree[v] = int(tree[left[v]]) + int(tree[right[v]])
        elif tree[v] == '-':
            tree[v] = int(tree[left[v]]) - int(tree[right[v]])
        elif tree[v] == '*':
            tree[v] = int(tree[left[v]]) * int(tree[right[v]])
        elif tree[v] == '/': # 정수로 계산
            tree[v] = int(tree[left[v]]) // int(tree[right[v]])
    return

for tc in range(1,11):
    # 정점의 총 수
    N = int(input())
    tree = [0]*(N+1)
    left = [0]*(N+1)
    right = [0]*(N+1)

    for _ in range(N):
        s = input().split()
        tree[int(s[0])] = s[1]
        # 정점이 연산자면(자식 노드가 있는 경우)
        if len(s) == 4:
            left[int(s[0])] = int(s[2])
            right[int(s[0])] = int(s[3])

    post_odrer(1)
    print(f'#{tc} {tree[1]}')
