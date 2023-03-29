# https://chaemi720.tistory.com/156

N = int(input())
A = set(input().split())
M = int(input())
arr = input().split()
for i in arr:
    if i in A:
        print(1)
    else:
        print(0)