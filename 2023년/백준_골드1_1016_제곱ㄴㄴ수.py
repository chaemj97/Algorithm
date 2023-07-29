'''
    접근법
    
'''
import sys
input = sys.stdin.readline

a,b = map(int,input().split())

arr = [i**2 for i in range(2,int(b**0.5)+1)]

num = [1]*(b-a+1)
for i in arr:
    n = a//i*i
    while n <= b:
        if n - a >= 0:
            num[n-a] = 0
        n += i
print(sum(num))