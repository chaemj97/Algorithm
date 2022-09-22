# 4153.직각 삼각형
# while True:
#     tri = list(map(int,input().split()))
#     tri.sort()
#     if tri[2] == 0:
#         break

#     if tri[2]**2 == tri[0]**2 + tri[1]**2:
#         print('right')
#     else:
#         print('wrong')
    
# 1259. 팰린드롬수
# while True:
#     num = input()
#     if num == '0':
#         break

#     if num == num[::-1]:
#         print('yes')
#     else:
#         print('no')

# 2231. 분해합
# N = int(input())

# for i in range(N):
#     answer = i + sum(map(int,str(i)))
#     if answer == N:
#         print(i)
#         break
# else:
#     print(0)

# 10828. 스택
# from sys import stdin
# input = stdin.readline

# N = int(input())
# stack = []
# for _ in range(N):
#     order = list(input().split())
#     if order[0] == 'push':
#         stack.append(order[1])
#     elif order[0] == 'pop':
#         if stack:
#             print(stack.pop())
#         else:
#             print(-1)
#     elif order[0] == 'size':
#         print(len(stack))
#     elif order[0] == 'empty':
#         if stack:
#             print(0)
#         else:
#             print(1)
#     elif order[0] == 'top':
#         if stack:
#             print(stack[-1])
#         else:
#             print(-1)

# 1978. 소수 찾기
# def check(x):
#     if x == 1:
#         return False
#     for j in range(2,int(x**0.5)+1):
#         if x%j == 0:
#             return False
#     return True

# N = int(input())
# arr = list(map(int,input().split()))

# answer = 0
# for i in arr:
#     if check(i):
#         answer += 1

# print(answer

# 11050 이항 계수 1
# N, K = map(int,input().split())
# answer = 1
# for i in range(K):
#     answer *= N-i
#     answer /= i+1
# print(int(answer))

# 2751. 수 정렬하기2
# N = int(input())
# arr = [int(input()) for _ in range(N)]
# arr.sort()
# for i in arr:
#     print(i)