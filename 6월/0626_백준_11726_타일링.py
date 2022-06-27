# https://chaemi720.tistory.com/185

from sys import stdin
input = stdin.readline

# 2Xn 크기의 직사각형
n = int(input())

# 결과
result = [0,1,2]

for i in range(3,n+1):
    result.append((result[i-1]+result[i-2])%10007)

print(result[n])