# https://chaemi720.tistory.com/159

# 정수 K개
K = int(input())
num = []
for _ in range(K):
    n = int(input())
    # 0이 아니면 넣고
    if n != 0:
        num.append(n)
    # 0이면 직전에 넣은 거 버리김
    else:
        num.pop()
print(sum(num))

# 시간 초과시
# from sys import stdin

# K = int(stdin.readline())
# total = []

# for _ in range(K):
#     n = int(stdin.readline())
#     if n == 0:
#         num.pop()
#     else:
#         num.append(n)

# print(sum(num))