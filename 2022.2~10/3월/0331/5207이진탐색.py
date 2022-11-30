# A[s:e+1] 리스트에서 t 찾기
# d : 오른쪽(1), 왼쪽(2)
def check(s,e,t,d):
    mid = (s+e)//2
    if t == A[mid]:
        if d == 0:
            result = 0
            return result
        else:
            result = 1
            return result

    if d == 1:
        if t < A[mid]:
            d = 2
            check(s,mid-1,t,d)
        else:
            result = 0
            return result
    elif d == 2:
        if t > A[mid]:
            d = 1
            check(mid+1,e,t,d)
        else:
            result = 0
            return result
    else:
        if t < A[mid]:
            d = 2
            check(s,mid-1,t,d)
        else:
            d = 1
            check(mid + 1, e, t, d)


# 테스트케이스 개수
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int, input().split()))

    # 조건 만족 개수
    cnt = 0
    result = 0
    for t in B:

        if check(0, N - 1, t, 0) == 1:
            cnt += 1

    print(f'#{tc} {cnt}')