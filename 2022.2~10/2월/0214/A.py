
# arr = [list(map(int,input().split())) for _ in range(5)]
# print(arr)

# 5 6 24 25 10
# 6 18 9 16 11
# 3 11 20 19 16
# 14 7 19 24 25
# 25 16 12 22 24

#  연습문제 1

# arr = [[5, 6, 24, 25, 10], [6, 18, 9, 16, 11], [3, 11, 20, 19, 16], [14, 7, 19, 24, 25], [25, 16, 12, 22, 24]]
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
#
# sum_v = 0
# for i in range(5):
#     for j in range(5):
#         # arr[i][j]
#         for d in range(4):
#             r = i + dr[d]
#             c = j + dc[d]
#             # r,c 의 좌표값이 정상일 때만 더해주기
#             if 0 <= r < 5 and 0 <= c < 5:
#                 # sum_v += abs(arr[i][j] - arr[r][c])
#                 tmp_v = arr[i][j] - arr[r][c]
#                 sum_v = sum_v + tmp_v if tmp_v > 0 else sum_v + (-tmp_v)
# print(sum_v)

# result = 0
# subset = [[0]*5 for _ in range(5)]
# for i in range(5):
#     for j in range(5):
#         for a,b in [[0,1],[-1,0],[0,-1],[1,0]]:
#              if 0 <= i+a <= 4 and 0 <= j+b <= 4:
#                  result += abs(arr[i][j] - arr[i+a][j+b])
# print(result)
# print("====================")
#


# 연습문제 2
# 부분집합 합 10인거로 변경
arr = [1,2,3,4,5,6,7,8,9,10]
N = 10
#모든 부분집합 1024개 확인
for i in range(2**N):
    # 2**N == 1<<N
    # i의 비트모양이 부분집합의 모양(부분집합에 포함되는 요소)
    # i의 각 비트를 검사
    sum_sub = 0
    subset = []
    for j in range(N):
        # i의 이진 표현의 j번째 비트를 확인
        if i & (1<<j): # 연산의 결과가 0이 아니라면, j번째 비트는 1
            #j번째 요소는 부분집합에 포함
            sum_sub += arr[j]
            subset.append(arr[j])
    if sum_sub == 10:
        # 부분집합 출력
        print(subset)
print("====================")
#
# # 재귀로 풀기
# # idx번째 요소가 부분집합에 포함되는지 결정
# #selected[] : 각 요소가 부분집합에 포함되는지 표시하는 배열
# def solve(idx, selected):
#     if idx == N: # 모든 요소(0~N~1번요소까지) 다 결정
#         # print(selected)
#         sum_sub = 0
#         subset = []
#         for i in range(N):
#             if selected[i]:
#                 sum_sub += arr[i]
#                 subset.append((arr[i]))
#         if sum_sub == 10:
#             print(subset,end=' ')
#             print()
#         return
#     # 우리가 해볼 수 있는 모든 경우의 수 고려
#     # idx 번째 요소를 부분집합에 포함
#     selected[idx] = 1
#     solve(idx + 1,selected)
#     # idx 번째 요소를 부분집합에 포함 X
#     selected[idx] = 0
#     solve(idx + 1, selected)
#
# solve(0,[0]*N)
# print("====================")
#
# # # 연습문제 3
# #
# N = 5 # 행열 한 변의 길이
# arr= [[0] * N for  _ in range(N)]
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
# # 다음 칸으로 이동하기 위한 방향을 나타내는 변수
# # 0: 우, 1: 하, 2: 좌, 3: 상
# dir =0 # 최초는 오른쪽으로 이동
# r, c = 0, 0 # 현재 위치
# num = 1
# # N*N 행렬에 1부터 N*N 까지 정수를 하나씩 넣기
# # 숫자를 행렬에 다 넣을 때 까지 계속 반복
# # 이동하고, 숫자 넣기
# while num <= N*N:
#     # 정상 범위이고 다른 숫자가 없으면, 숫자할당
#     if 0 <= r < N and 0 <= c < N and not arr[r][c]:
#         arr[r][c] = num
#         num += 1
#     else:
#         # 정상 범위가 아니니깐 이동방향 바꾸기, 그리고 정상범위 안으로 돌리기
#         r -= dr[dir]
#         c -= dc[dir]
#         # 지금 가는 방향으로 계속 가면 또 범위 벗어남
#         dir = (dir + 1) % 4
#
#     r += dr[dir]
#     c += dc[dir]
#
# for row in arr:
#     print(row)












