# https://chaemi720.tistory.com/150

# M*N 크기의 보드
N,M = map(int,input().split())
jimin = [input() for _ in range(N)]

min_cnt = 10**10

# # (r,c)는 시작 위치
# for r in range(N-8+1):
#     for c in range(M-8+1):
#         # w시작인지, b시작인지 동시에 비교? -> 반대로 뒤집힐 때도 있으니 단정X
#         one = 0
#         two = 0
#         # (i,j)는 비교 위치
#         for i in range(r,r+8):
#             for j in range(c,c+8):
#                 # 번갈아 가면서 wbwb비교? bwbw비교?
#                 if (i+j)%2:
#                     if jimin[i][j] == 'B':
#                         one += 1
#                     else:
#                         two += 1
#                 else:
#                     if jimin[i][j] == 'W':
#                         one += 1
#                     else:
#                         two += 1
#         # 비교 다 한 후 최솟값인가?
#         min_cnt = min(min_cnt,one,two)

# (r,c)는 시작 위치
for r in range(N-8+1):
    for c in range(M-8+1):
        # b로 시작, w로 시작
        one = 0
        two = 0
        # (i,j)는 비교 위치
        for i in range(r,r+8):
            # num1 + num2 : WBWBWBWB와 일치하는 갯수
            num1 = [jimin[i][c+0], jimin[i][c+2], jimin[i][c+4], jimin[i][c+6]].count('B')
            num2 = [jimin[i][c+1], jimin[i][c+3], jimin[i][c+5], jimin[i][c+7]].count('W')
            if i%2:
                one += 8-num1-num2
                two += num1+num2
            else:
                two += 8 - num1 - num2
                one += num1 + num2
        # 비교 다 한 후 최솟값인가?
        min_cnt = min(min_cnt,one,two)

print(min_cnt)