def f(i,N,K): # i부분집합에 포함될지 결정할 원소의 인덱스, N 전체 원소개수, K 찾는 합
    global cnt
    cnt += 1
    if i == N : # 한개의 부분집합 완성
        # print(bit, end=' ')
        sum = 0
        for j in range(N):
            if bit[j]:
                sum += a[j]

        if sum == K: # 찾는 합이면
            for j in range(N):
                if bit[j]:
                    print(a[j], end=' ')
            print()
    else:
        bit[i] = 1
        f(i+1,N,K)
        bit[i] = 0
        f(i+1,N,K)
    return
a = [1,2,3,4,5,6,7,8,9,10]
N = len(a)
bit = [0]*N
cnt = 0
f(0,N,10)
print('cnt = ',cnt)