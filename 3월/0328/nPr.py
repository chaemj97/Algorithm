def f(m,n,k): # 순열 p[m]을 채우는 함수, n개 중 k개 고르기
    global cnt
    if m == k:
        cnt += 1
        print(p)
    else:
        for i in range(n): # used에서 사용하지 않은 숫자 검색
            if used[i] == 0: # 앞에서 사용하지 않은 숫자인 경우
                used[i] = 1 # 사용함으로 표시
                p[m] = a[i] # p[m] 결정
                f(m+1,n,k)
                used[i] = 0 # a[i]를 다른 위치에서 사용할 수 있도록 함
    return

a = [1,2,3,4,5]
p = [0]*3
used = [0]*len(a)
cnt = 0
f(0,5,3) # 5P3
print(cnt)