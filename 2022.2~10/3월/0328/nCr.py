'''
def nCr(n,r,s): # n개에서 r개를 고르는 조합, s선택할 수 있는 구간의 시작
    global cnt
    if r == 0:
        cnt += 1
        print(comb)
    else:
        for i in range(s,n-r+1):
            comb[r-1] = A[i]
            nCr(n,r-1,i+1)
n = 5
r = 3
comb = [0]*r
A = [i for i in range(1,n+1)]
cnt = 0
nCr(n,r,0)
print(cnt) # 10
'''

'''
# 순서대로 나열

# # n개에서 r개를 고르는 조합, s선택할 수 있는 구간의 시작, k 고른 개수
def nCr2(n,r,s,k):
    if k == r:
        print(comb2)
    else:
        for i in range(s,n-r+k+1): # n-r+k 선택할 수 있는 구간의 끝
            comb2[k] = A2[i]
            nCr2(n,r,i+1,k+1)

n2 = 4
r2 = 3
A2 = [i for i in range(1,n2+1)]
comb2 = [0]*r2
nCr2(n2,r2,0,0)
'''

# 5개 중 3개 뽑기
for i in range(0,3): # j,k로 선택될 원소를 남김
    for j in range(i+1,4): # k로 선택될 원소를 남김
        for k in range(j+1,5):
            print(i,j,k)