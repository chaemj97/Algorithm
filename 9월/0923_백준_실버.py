# # 10845 큐
# from collections import deque
# from sys import stdin
# input=stdin.readline
# N = int(input())

# que = deque()

# for _ in range(N):
#     order = list(input().split())
#     if order[0] == 'push':
#         que.append(order[1])
#     elif order[0] == 'pop':
#         if que:
#             print(que.popleft())
#         else:
#             print(-1)
#     elif order[0] == 'size':
#         print(len(que))
#     elif order[0] == 'empty':
#         if que:
#             print(0)
#         else:
#             print(1)
#     elif order[0] == 'front':
#         if que:
#             print(que[0])
#         else:
#             print(-1)
#     else:
#         if que:
#             print(que[-1])
#         else:
#             print(-1)

# 10866 덱
# from collections import deque
# from sys import stdin
# input=stdin.readline

# N = int(input())

# que = deque()

# for _ in range(N):
#     order = list(input().split())
#     # print('aa',order)
#     if order[0] == 'push_front':
#         que.appendleft(order[1])
#     if order[0] == 'push_back':
#         que.append(order[1])
#     elif order[0] == 'pop_front':
#         if que:
#             print(que.popleft())
#         else:
#             print(-1)
#     elif order[0] == 'pop_back':
#         if que:
#             print(que.pop())
#         else:
#             print(-1)
#     elif order[0] == 'size':
#         print(len(que))
#     elif order[0] == 'empty':
#         if que:
#             print(0)
#         else:
#             print(1)
#     elif order[0] == 'front':
#         if que:
#             print(que[0])
#         else:
#             print(-1)
#     elif order[0] == 'back':
#         if que:
#             print(que[-1])
#         else:
#             print(-1)

# 11650 좌표 정렬하기
# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]

# arr.sort(key=lambda x : (x[0],x[1]))
# for x,y in arr:
#     print(x,y)

# 10816 숫자 카드 2
# N = int(input())
# sang = list(map(int,input().split()))
# M = int(input())
# arr = list(map(int,input().split()))

# result = {}
# for i in sang:
#     if i in result:
#         result[i] += 1
#     else:
#         result[i] = 1
#     # result[i] = sang.count(arr[i]) # 시간 복잡도 O(N)

# for j in arr:
#     r = result.get(j,0)
#     print(r,end=' ')
