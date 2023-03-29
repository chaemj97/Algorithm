# 최소힙
def min_heap(v):
    global last
    last += 1
    tree[last] = v
    # 자손
    c = last
    # 부모
    p = c//2
    # 부모가 자식보다 큰 경우 부모 자식 바꾸기
    while p >= 1 and tree[p] > tree[c]:
        tree[p],tree[c] = tree[c],tree[p]
        # 바꾸면 부모노드가 자식노드가 되는 트리로 보기
        c = p
        p = c//2

# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # N개의 서로 다른 자연수
    N = int(input())
    arr = list(map(int,input().split()))

    tree = [0]*(N+1)
    # 마지막 정점 인덱스
    last = 0
    # 노드 추가
    # 최소 이진힙에 저장
    for i in arr:
        min_heap(i)

    # 마지막 노드의 조상 노드에 저장된 정수의 합 구하기
    sum = 0
    # 부모 노드번호는 자식노드//2
    while last > 1:
        last //= 2
        sum += tree[last]

    print(f'#{tc} {sum}')
