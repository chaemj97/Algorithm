# https://chaemi720.tistory.com/180

from sys import stdin

input = stdin.readline

# 동전의 종류, 동전 가치의 합
N,K = map(int,input().split())
value = [int(input()) for _ in range(N)]

# ----------------------------------
# 이진 탐색
# # 필요한 동전 개수의 최솟값
# cnt = 0

# # K보다 작은 값 중 가장 큰 값 찾기
# def check(start,end):
#     while start <= end:
#         mid = (start + end)//2
#         if value[mid] <= K:
#             start = mid +1
#         else:
#             end = mid -1
#     return end

# while K > 0:
#     # K보다 작은 값 중 가장 큰 값을 찾기
#     coin = value[check(0,N-1)]

#     # K가 coin보다 작아질 때까지 빼주기
#     while K >= coin:
#         K -= coin
#         cnt += 1

# print(cnt)

# ----------------------------------
# for문
# 필요한 동전 개수의 최솟값
cnt = 0
for idx in range(N-1,-1,-1):
    cnt += K // value[idx]
    K = K % value[idx]

print(cnt)