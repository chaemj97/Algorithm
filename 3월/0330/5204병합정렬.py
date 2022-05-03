def merge_sort(a):
    global cnt
    if len(a) == 1:
        return a
    else:
        mid = len(a)//2
        left = merge_sort(a[:mid])
        right = merge_sort(a[mid:])
        if left[-1] > right[-1]:
            cnt += 1
        return merge(left,right)

def merge(left,right):
    result = []
    l = r = 0
    while l < len(left) or r < len(right):
        if l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        elif l < len(left):
            result.append(left[l])
            l += 1
        elif r < len(right):
            result.append(right[r])
            r += 1
    return result

# 테스트 케이스 수
T = int(input())
for tc in range(1,T+1):
    # 정수의 개수
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    m = merge_sort(arr)

    print(f'#{tc} {m[N//2]} {cnt}')