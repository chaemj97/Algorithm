'''
    접근법 1
        바이토닉 부분 수열 : 증가했다가 감소하는 수열
        dp_inc[i] : arr[0]~arr[i]에서 증가하는 수열의 개수
        dp_dec[i] : arr[i]~arr[N-1]에서 감소하는 수열의 개수
        
        바이토닉 부분 수열 : dp_inc[i] + dp_dec[N-1-i] - 1
'''

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
# 증가
# dp_inc[i] : index 0부터 index i까지 증가하는 수열의 개수
dp_inc = [1]*N

# 감소
# dp_inc[i] : index i부터 index N-1까지 감소하는 수열의 개수
arr_reverse = arr[::-1]
dp_dec = [1]*N

for i in range(N):
    for j in range(i):
        # 증가
        if arr[i] > arr[j]:
            dp_inc[i] = max(dp_inc[i],dp_inc[j]+1)

        # 감소
        if arr_reverse[i] > arr_reverse[j]:
            dp_dec[i] = max(dp_dec[i],dp_dec[j]+1)


# 증가부분 감소부분 합치기
result = []
for i in range(N):
    # arr[i]가 두 번 count 되었기 때문에 -1
    result.append(dp_inc[i] + dp_dec[N-1-i]-1)

# 가장 긴 수열
print(max(result))
