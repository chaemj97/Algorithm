# https://chaemi720.tistory.com/161

from sys import stdin

# 수행해야 하는 연산의 수
M = int(input())
S = set()

for _ in range(M):
    wordNum = stdin.readline().split()
    # 추가
    if wordNum[0] == 'add' or (wordNum[0] == 'toggle' and int(wordNum[1]) not in S):
        S.add(int(wordNum[1]))
    # 삭제
    elif wordNum[0] == 'remove' or (wordNum[0] == 'toggle' and int(wordNum[1]) in S):
        S.discard(int(wordNum[1]))
    # 체크
    elif wordNum[0] == 'check':
        if int(wordNum[1]) in S:
            print(1)
        else:
            print(0)
    # 집합 all
    elif wordNum[0] == 'all':
        S = {1,2,3,4,5,6,7,8,9,10,
        11,12,13,14,15,16,17,18,19,20}
    # 공집합
    elif wordNum[0] == 'empty':
        S = set()