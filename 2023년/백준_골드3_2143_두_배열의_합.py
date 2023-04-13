'''
    접근법 1
        A,B의 각각 원소마다 누적합 구학
        ex) 
            A = [1,3,1,2]
            A_sum = [1,1+3,1+3+1,1+3+1+2,3,3+1,3+1+2,1,1+2,2]
                  = [1,4,5,7,3,4,6,1,3,2]
                  
        T = A_sum[i] + B_sum[j] (i = 0,...,len(A_sum)-1, j = 0,...,len(B_sum)-1)
        T - A_sum[i] = B_sum[j]
        B_sum에서 T - S_sum[i]의 위치 이분 탐색

'''
import bisect
import sys
input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

# 누적합 구하기
A_sum = []
B_sum = []
for i in range(n):  
    s = A[i]
    A_sum.append(s)
    for j in range(i+1,n):
        s+=A[j]
        A_sum.append(s)
for i in range(m):  
    s = B[i]
    B_sum.append(s)
    for j in range(i+1,m):
        s+=B[j]
        B_sum.append(s)
A_sum.sort()
B_sum.sort()   

answer = 0
# T = A_sum[i] + B_sum[j]
# T - A_sum[i] = B_sum[j]
for i in range(len(A_sum)):
    # A_sum[i]와 더해서 T가 될 B_sum[j] 최소 수 위치
    l = bisect.bisect_left(B_sum, T-A_sum[i])
    # A_sum[i]와 더해서 T가 될 B_sum[j] 최대 수 위치+1
    r = bisect.bisect_right(B_sum, T-A_sum[i])
    answer += r - l
    
print(answer)