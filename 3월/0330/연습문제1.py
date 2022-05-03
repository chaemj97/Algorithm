# arr의 start와 end 범위에서
# 파티션 정해서 큰 값, 작은 값 분류하고
# 피벗 위치를 반환하는 함수
def partition(arr,start,end):
    pivot = arr[start]
    i = start
    j = end
    # i는 오른쪽으로 이동하면서 큰 값 찾기
    # j는 왼쪽으로 이동하면서 작은 값 찾기
    while i <= j:
        # 피벗보다 작거나 같으면 i 증가, 크면 멈추기
        while arr[i] <= pivot:
            i += 1
        # 피벗보다 크거나 같으면 i 감소, 작으면 멈추기
        while arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]

    arr[start],arr[j] = arr[j],arr[start]
    return pivot

def quick_sort(arr,start,end):
    # 더 이상 자를 수 없음
    if start >= end:
        return
    # 피벗을 선정하고
    # 피벗을 기준으로 큰값과 작은값 구분
    pivot = partition(arr,start,end)
    # 작은 부분 정렬
    quick_sort(arr,start,pivot-1)
    # 큰 부분 정렬
    quick_sort(arr,pivot+1,end)
    pass

arr = [7,2,6,4,9,3,8,1,5,0]
N = len(arr)

quick_sort(arr,0,N-1)
print(arr)