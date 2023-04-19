'''
    접근법 1
        첫번째 용액 고정 후 두번째 용액을 이분 탐색으로 찾기
            -> 시간이 많이 걸림
            
    접근법 2
        투 포인트로 동시에 찾기

'''

import sys
input = sys.stdin.readline

N = int(input())
# 오름차순 정렬
arr = sorted(list(map(int,input().split())))

'''
result = []
min_sum = float('inf')

for i in range(N-1):
    # 첫번째 용액 고정
    one = arr[i]
    l = i+1
    r = N-1
    while l <= r:
        mid = (l+r)//2
        # 두번째 용액
        two = arr[mid]
        
        # 두 용액 섞기
        s = one + two
        # 0에 가까우면 갱신
        if abs(s) < abs(min_sum):
            min_sum = s
            result = [one,two]
        
        # 0이면 끝내기
        if s == 0:
            print(*result)
            sys.exit()
        
        if s > 0:
            r = mid - 1
        else:
            l = mid + 1 

print(*result)
'''

#######################################
# 둘 다 이동
s,e = 0,N-1
min_sum = abs(arr[s] + arr[e])
answer = [arr[s],arr[e]]
while s < e:
    mix = arr[s] + arr[e]
    # 0에 가장 가깝다
    if abs(mix) <= min_sum:
        min_sum = abs(mix)
        answer = [arr[s],arr[e]]
        
    # 합이 음수면
    if mix < 0:
        s += 1
    else:
        e -= 1
print(*answer)