# https://chaemi720.tistory.com/192

# 시간이 num일 때 심사 받을 수 있는 사람 수 구하기
def cnt(num,times):
    c = 0
    for t in times:
        c += num//t
    return c

def solution(n, times):
    times.sort()
    
    l = 0
    r = n*times[0]

    while l < r:
        mid = (l + r)//2
        cc = cnt(mid,times)
        # cc 시간 안에 모두 심사 못 함 -> 시간을 늘려야 함
        if cc < n:
            l = mid + 1
        else:
            r = mid 
    
    return r