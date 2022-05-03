'''
def in_order(v):
    if v: # 0번 정점이 없으므로, 0번은 자식이 없는 경우를 표시
        in_order(ch1[v])
        print(tree[v],end='') # visit(v)
        in_order(ch2[v])

# 완전 이진 트리
for tc in range(1,11):
    # 정점의 총 수
    last = int(input())

    # 완전 이진 트리 만들기
    tree = [0]*(last+1)
    # 왼쪽 자식
    ch1 = [0]*(last+1)
    # 오른쪽 자식
    ch2 = [0]*(last+1)

    for _ in range(last):
        s = input().split()
        tree[int(s[0])] = s[1]
        if len(s) >= 3:
            # 왼쪽 자식이 있다면
            ch1[int(s[0])] = int(s[2])
        if len(s) == 4:
            ch2[int(s[0])] = int(s[3])
    print(f'#{tc} ',end='')
    in_order(1)
    print()
'''

'''
# 보충
def inorder(v):
    if v:
        inorder(left[v])
        print(alpha[v],end='')
        inorder(right[v])
    return

for tc in range(1,11):
    N = int(input())
    alpha = ['']*(N+1) # 알파벳
    left = [0]*(N+1) # 왼쪽 자식
    right = [0]*(N+1) # 오른쪽 자식

    for i in range(N):
        temp = list(input().split())
        idx = int(temp[0])
        alpha[idx] = temp[1]
        if idx*2 <= N: # 왼쪽 자식 존재
            left[idx] = int(temp[2])
            if idx*2+1 <= N: # 오른쪽 자식 존재
                right[idx] = int(temp[3])

    print(f'#{tc}',end=' ')
    inorder(1)
    print()
'''
# heapq 라이브러리 있음

# 보충 짧은 답
# 왼쪽자식번호, 오른쪽자식번호 사용 안함
def in_order2(n):
    global word
    if n <= N:
        in_order2(n*2)
        word += arr[n-1][1]
        in_order2(n*2+1)

for tc in range(1,11):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    print(arr)
    word = ''
    in_order2(1)
    print(f'#{tc} {word}')

