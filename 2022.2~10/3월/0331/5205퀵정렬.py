def quickSort(a,begin,end):
    if begin < end:
        p = partition(a,begin,end)
        quickSort(a,begin,p-1)
        quickSort(a,p+1,end)

def partition(a,begin,end):
    # 중간 값을 pivot으로 두기
    # pivot보다 작은 값은 pivot의 왼쪽에 두기
    # pivot보다 큰 값은 pivot의 오른쪽에 두기
    pivot = begin
    L = begin
    R = end
    while L < R:
        # 왼쪽에서부터 pivot보다 큰 값 찾기
        while L < R and a[L] <= a[pivot]:
            L += 1
        # 오른쪽에서부터 pivot보다 작은 값 찾기
        while a[R] > a[pivot]:
            R -= 1
        if L < R:
            # pivot보다 작은 건 왼쪽, 큰 건 오른쪽에 두기기
            a[L], a[R] = a[R], a[L]
    # 피봇을 작은것들 집합과 큰 것들 집합 사이에 두기
    a[pivot], a[R] = a[R], a[pivot]
    return R

# 테스트 케이스 수
T = int(input())
for tc in range(1,T+1):
    # 정수의 개수
    N = int(input())
    arr = list(map(int,input().split()))
    quickSort(arr,0,N-1)
    A = arr
    print(f'#{tc} {A[N//2]}')