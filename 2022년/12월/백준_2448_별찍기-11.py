
N = int(input())

# 기본형
graph = [[" ", " ","*"," "," "],[" ", "*"," ","*"," "],["*", "*","*","*","*"]]

# 
def recursive(n,before):
    after = [[" "] * (2*2*n-1) for _ in range(2*n)]
    # 왼쪽 별 무리
    for i in range(n):
        after[i][n:n+2*n-1] = before[i]
    # 오른쪽 별 무리
    k = 0
    for i in range(n,2*n):
        after[i][:2*n] = before[k]
        after[i][2*n:2*n+len(before[k])] = before[k]
        k += 1

    # 다 완성?
    if 2*n == N:
        return after
    return recursive(2*n,after)

# N이 3일때가 기본형, 그다음은 재귀
if N == 3:
    result = graph
else:
    result = recursive(3,graph)

# 출력
for i in result:
    print("".join(i))