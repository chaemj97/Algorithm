

from sys import stdin
from collections import deque
input = stdin.readline

# 테스트 케이스
T = int(input())
for tc in range(T):
    # 수행할 함수
    p = input().rstrip()
    # RR은 의미없는 수행
    p = p.replace('RR', '')

    # 배열에 수 개수
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(','))

    # 빈 배열이라면 수행 할 필요 없음
    if n == 0:
        # 빈 배열에 첫번째 숫자 버릴 수 없음 error
        if 'D' in p:
            print('error')
        else:
            print('[]')
        continue

    # D가 배열 길이보다 많이 있어도 error
    if p.count('D') > len(arr):
        print('error')
    else:
        reverse = False
        for i in p:
            # 뒤집기
            if i == 'R':
                reverse = not reverse
            # 맨 앞 버리기
            else:
                if reverse:
                    arr.pop()
                else:
                    arr.popleft()
        # 출력
        if reverse:
            arr.reverse()
        print("["+",".join(arr)+"]")

