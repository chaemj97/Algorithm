from sys import stdin
input = stdin.readline

# nCm 구하기
n, m = map(int,input().split())
com = 1
bin = 1
for i in range(1,m+1):
    com *= (n-i+1)
    bin *= i

print(int(com//bin))