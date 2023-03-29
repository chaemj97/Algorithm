def f(i,s):
    global cnt
    if i == N:
        if s == 0:# 목표값을 찾으면
            cnt += 1
        return
    else:
        bit[i] = 1
        f(i+1,s+a[i])
        bit[i] = 0
        f(i+1,s)

N = int(input())
a = list(map(int,input().split()))
bit = [0]*N
t = 0 # 찾고자 하는 합
cnt = 0
f(0,0)
print(cnt)