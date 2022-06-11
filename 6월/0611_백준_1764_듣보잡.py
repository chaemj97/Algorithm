# https://chaemi720.tistory.com/160

# import
# # 듣도 못한 사람 N, 보도 못한 사람 M
# N,M = map(int,input().split())
# nohear = set(input() for _ in range(N))
# nosee = set(input() for _ in range(M))

# # nohear과 nosee의 공통 찾기
# no = nohear&nosee

# # 듣보잡의 수
# print(len(no))
# # 듣보잡 명단(사전식 정렬)
# for n in sorted(no):
#     print(n)


# sys.stdin
from sys import stdin
# 듣도 못한 사람 N, 보도 못한 사람 M
N,M = stdin.readline().rstrip().split()
nohear = set(stdin.readline().rstrip() for _ in range(int(N)))
nosee = set(stdin.readline().rstrip() for _ in range(int(M)))

# nohear과 nosee의 공통 찾기
no = nohear&nosee

# 듣보잡의 수
print(len(no))
# 듣보잡 명단(사전식 정렬)
for n in sorted(no):
    print(n)