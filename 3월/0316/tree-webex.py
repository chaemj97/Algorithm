V = 13
edges = list(map(int,'1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'.split()))
# 인덱스가 부모의 정점 번호가 되는 배열 2개 선언해서 사용
arr = [[0]*(V+1) for _ in range(2)]
tree = [0]*32
# arr[0] : 왼쪽 자식 정보
# arr[1] : 오른쪽 자식 정보

for i in range(0,len(edges),2):
    # edges[i]가 부모노드 번호
    # edges[i+1]이 자식 노드 번호
    if arr[0][edges[i]]: # 왼쪽 자식 정보가 있으면 오른쪽 자식 설정
        arr[1][edges[i]] = edges[i+1]
    else:
        arr[0][edges[i]] = edges[i+1]

    # 만약에 부모노드가 없으면 루트
    if edges[i] not in tree:
        tree[1] = edges[i]
    # 부모노드의 왼쪽자식이 있으면, 오른쪽 자식으로 설정
    # 아니면 왼쪽 자식으로 설정
    # 배열형태에서 왼쪽 자식의 인덱스를 확인하려면 부모노드의 인덱스를 알아야 함
    p_idx = tree.index(edges[i])
    # 왼쪽 자식의 인덱스 : 부모인덱스 * 2
    # 왼쪽 자식 있으면 오른쪽에 넣기
    if tree[p_idx*2]:
        tree[p_idx*2+1] = edges[i+1]
    else:
        tree[p_idx*2] = edges[i+1]

print(tree)

print(arr)
# 입력 제대로 받았으니 순회

def pre_order(v):
    # arr에 정점이 없는 경우는 0으로 저장되어있음
    if v != 0:
        # 정점이 있다면, 작업하기 -> 전위순회
        # 현재 정점 작업(출력)
        print(v,end=' ')
        # 왼쪽 자식 탐색
        pre_order(arr[0][v])
        # 오른쪽 자식 탐색
        pre_order(arr[1][v])

def pre_order2(idx):
    # tree에 정점이 없는 경우는 0으로 저장되어있음
    if tree[idx] != 0:
        # 정점이 있다면, 작업하기 -> 전위순회
        # 현재 정점 작업(출력)
        print(tree[idx],end=' ')
        # 왼쪽 자식 탐색
        pre_order(idx*2)
        # 오른쪽 자식 탐색
        pre_order(idx*2+1)


# pre_order(1)
pre_order(1)
print()
print('----------')
pre_order2(1)