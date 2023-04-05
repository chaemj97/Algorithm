'''
    접근법 1
        행렬 곱을 사용하여 계산

'''

import sys
input = sys.stdin.readline

N,B = map(int,input().split())
A = list(list(map(int,input().split())) for _ in range(N))

# 행렬 제곱
def matrix_power(arr,n):
    if n == 1:
        # 각 원소 1000으로 나눈 나머지
        for r in range(len(arr)):
            for c in range(len(arr[0])):
                arr[r][c] = arr[r][c]%1000
        return arr
    # n이 짝수
    elif n%2 == 0:    
        return matrix_power(matrix_cal(arr,arr),n//2)
    # n이 홀수
    else:
        return matrix_cal(matrix_power(arr,n-1),arr)
    
# 행렬 곱
def matrix_cal(arr_one,arr_two):
    result = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            n = 0
            for i in range(N):
                n += arr_one[r][i]*arr_two[i][c]
            result[r][c] = n%1000
    return result

result = matrix_power(A,B)
for i in result:
    print(*i)