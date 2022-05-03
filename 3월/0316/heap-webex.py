heap = [0]*16
# 마지막요소를 가리키는 변수
heapcount = 0

# 최대힙
def heap_push(value):
    global heapcount
    # 완전이진트리를 유지해야 하므로 마지막 자리에 넣기
    heapcount += 1
    heap[heapcount] = value
    # 부모노드가 삽입한 요소보다 작으면 자리바꾸기
    current = heapcount
    parent = heapcount//2
    # 자리를 바꾸고 나서 부모노드와 비교해서
    # 부모노드가 작으면 자리 바꾸기 작업을 계속 수행
    # 스스로가 루트이면 멈춰!!
    # 부모노드 값이 작으면 계속 반복
    while parent > 0 and heap[parent] < heap[current]:
        heap[parent], heap[current] = heap[current], heap[parent]
        # 바꿨으니 부모노드가 현재노드가 되는 것,
        # 새로운 부모노드 인덱스 계산
        current = parent
        parent = current // 2




def heappop():
    global heapcount
    result = heap[1]
    # 맨 마지막 요소를 루트로 올림
    heap[1] = heap[heapcount]
    # 마지막 요소는 뺐으니
    heapcount -= 1
    # 자식 요소 중에 큰 값과 비교해서 작으면 교체
    parent = 1
    child = parent*2
    # 만약에 오른쪽 자식이 있으면, 왼쪽 자식과 오른쪽 자식을 비교해서
    # child를 결정
    if child+1 <= heapcount:
        if heap[child+1] > heap[child]:
            child += 1
    # child : 자식중에 더 큰 값을 가진 자식의 인덱스

    while child <= heapcount and heap[child] > heap[parent]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent*2
        if child + 1 <= heapcount:
            if heap[child + 1] > heap[child]:
                child += 1
    return result

heap_push(7)
print(heap)
heap_push(2)
print(heap)
heap_push(4)
print(heap)
heap_push(3)
print(heap)
heap_push(1)
print(heap)
heap_push(6)
print(heap)
heap_push(5)
print(heap)
print(heappop())
print(heap)
print(heappop())
print(heappop())
print(heappop())
print(heappop())
print(heappop())
print(heap)


