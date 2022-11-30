# i 부분집합에 포함될지 결정할 원소의 인덱스, N 전체 원소개수, s 이전까지 고려된 원소의 합, t 목표값, rs 고려하지 않은 원소들의 합
def f(i,N,s,t,rs):
    global cnt
    cnt += 1
    if s == t: # 목표값을 찾으면
        for j in range(N):
            if bit[j]:
                print(a[j],end=' ')
        print()
    elif i == N: # 더 이상 고려할 원소가 없으면
        return
    elif s > t: # 고려한 원소의 합 s가 이미 목표를 초과한 경우
        return
    elif s+rs < t:
        return
    else:
        bit[i] = 1
        f(i+1,N,s+a[i],t,rs-a[i])
        bit[i] = 0
        f(i+1,N,s,t,rs-a[i])
    return

N = 10
a = [x for x in range(1,N+1)]
bit = [0]*N
t = 27 # 찾고자 하는 합
cnt = 0
f(0,N,0,t,sum(a))
print('cnt = ',cnt)