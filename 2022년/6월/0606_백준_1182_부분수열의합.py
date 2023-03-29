
from itertools import combinations

# N개의 정수로 이루어진 수열, 부분수열 중 수열의 원소 합이 S 되는 경우의 수 구하기
N,S = map(int,input().split())
sequence = list(map(int,input().split()))

cnt = 0
# 조합으로 풀기
# 부분집합의 원소의 개수가 i인 부분집합의 집합 구하기
for i in range(1,len(sequence)+1):
    comb = list(combinations(sequence,i))
    # 각 부분집합의 합이 S인가 확인
    for com in comb:
        if sum(list(com)) == S:
            cnt += 1

print(cnt)
