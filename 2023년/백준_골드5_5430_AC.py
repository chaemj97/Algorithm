'''
    접근법 1
        구현문제
        R이 나올때마다 .reverse를 하면 시간초과 
        -> reverse가 True이면 뒤에서 버리기 (pop)
        -> False이면 앞에서 버리기 (popleft)

'''
from collections import deque
import sys
input = sys.stdin.readline

# 테스트 케이스의 개수
T = int(input())
for _ in range(T):
    # 수행할 함수
    p = input().rstrip()
    # RR은 의미없는 수행
    p = p.replace('RR','')
    
    # 배열에 들어있는 수의 개수
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(','))
    
    # D가 배열 길이보다 많이 있어도 error
    if p.count('D') > n:
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
            
    
    