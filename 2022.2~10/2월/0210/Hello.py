# arr : 정렬할 list
def BubbleSort(arr):
    N = len(arr)
    # 범위의 끝 위치
    for i in range(N-1,0,-1):
        for j in range(0,i):
            # 왼쪽 원소가 더 크면 오른쪽 원소와 교환
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [5,1,2,4,3]
print(BubbleSort(arr))
# [1, 2, 3, 4, 5]

# A : 입력 배열
def CountingSort(A):
    k = len(A)
    # result : 정렬된 배열
    result = [0]*k
    # 카운트 배열
    C = [0]*(k+1)

    # 각 항목들의 발생 횟술르 세기
    for i in range(len(A)):
        C[A[i]] += 1
    # 누적합 구하기
    for i in range(1,len(C)):
        C[i] += C[i-1]
    # 대입
    for i in range(len(result)-1,-1,-1):
        C[A[i]] -= 1
        result[C[A[i]]] = A[i]

    return result

A = [0,4,1,3,1,2,4,1]
print(CountingSort(A))
# [0, 1, 1, 1, 2, 3, 4, 4]

def SelectionSort(arr):
    N = len(arr)
    for i in range(N-1):
        minIdx = i
        for j in range(i+1,N):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    return arr

A = [64, 25, 10, 22, 11]
print(SelectionSort(A))
