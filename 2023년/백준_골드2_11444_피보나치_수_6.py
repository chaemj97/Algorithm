'''
    접근법 1
        https://chaemi720.tistory.com/281
'''

import sys
input = sys.stdin.readline

# 행렬 제곱
def power(adj,n):
    if n == 1:
        return adj
    # n이 짝수인 경우
    elif n%2 == 0:
        return power(multi(adj,adj),n//2)
    # n이 홀수인 경우
    else:
        return multi(power(adj,n-1),adj)

# 행렬의 곱셈
def multi(a,b):
    temp = [[0]*len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            s = a[i][0]*b[0][j]
            for k in range(2):
                s += a[i][k]*b[k][j]
            temp[i][j] = s%1000000007
    return temp
    

N = int(input())
# 초기 행렬
adj = [[1,1],[1,0]]
# 초기값
start = [[1],[0]]
if N < 3:
    print(1)
else:
    print(multi(power(adj,N-1),start)[0][0])