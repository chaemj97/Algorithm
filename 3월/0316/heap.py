'''
최대 100개의 정수
최대힙
'''

# 삽입
def enq(n):
    global last
    last += 1
    tree[last] = n # 완전이진트리 유지
    c = last # 새로 추가된 정점을 자식으로
    p = c//2
    while p>=1 and tree[p] < tree[c]: # 부모가 있고, 자식의 키 값이 더 크면 교환
        tree[p], tree[c] = tree[c],tree[p]
        c = p
        p = c//2
def deq():
    global last
    tmp = tree[1] # 루트의 key 값
    tree[1] = tree[last] # 마지막 정점의 키를 루트에 복사
    last -= 1 # 마지막 정점 삭제
    # 부모 > 자식 규칙 유지
    p = 1
    c = p*2 # 왼쪽자식노드 번호
    while c <= last: # 왼쪽자식이 존재하는가?
        if c+1 <= last and tree[c] < tree[c+1]: # 오른쪽 자식노드도 있고 더 크면
            c += 1 #오른쪽 자식 선택
        if tree[p] < tree[c]: # 자식의 키 값이 더 크면 교환
            tree[p],tree[c] = tree[c],tree[p]
            p = c
            c = p*2
        else:
            break
    return tmp

# 포화이진트리의 정점번호 1~100
tree = [0]*10
last = 0 # 마지막 정점 번호

enq(3)
enq(2)
enq(4)
enq(7)
enq(5)
enq(1)
enq(9)
print(tree)
# print(tree[1])
while last>0:
    print(last)
    print(deq(),tree[1])
    print(tree)
