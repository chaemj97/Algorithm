N = 5
arr = [4,2,1,5,3]

# 인덱스 이동하기
def sort(arr,idx,N):
    # idx 번째 자리에 들어갈 요소 찾아 idx번째 요소랑 자리 바꿔주기
    if idx >= N:
        print(arr)
        print('끝')
        return
    # print(arr[idx],end = ' ')
    # idx 포함 뒤쪽에 있는 원소 중 제일 작은 값 찾기
    min_idx = idx
    for i in range(idx,N):
        if arr[min_idx] > arr[i]:
            min_idx = i
    arr[min_idx], arr[idx] = arr[idx], arr[min_idx]
    sort(arr,idx+1,N)
sort(arr,0,N)
