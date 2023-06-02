'''
    접근법
        t를 s로 만들기
        1. 문자열 뒤에 A를 추가한다 -> 문자열 뒤에 A면 뺀다
        2. 문자열을 뒤집고 뒤에 B를 추가한다 -> 문자열 뒤에 B면 빼고 뒤집는다
    
'''

import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

answer = 1
# s와 t가 같으면 멈추기
while s != t:
    # 문자열 뒤에 A를 추가한다 -> 문자열 뒤에 A면 뺀다
    if t[-1] == 'A':
        t = t[:-1]
    # 문자열을 뒤집고 뒤에 B를 추가한다 -> 문자열 뒤에 B면 빼고 뒤집는다
    elif t[-1] == 'B':
        t = t[:-1]
        t = t[::-1]
    else:
        answer = 0
        break
    # t가 s보다 짧으면 t를 s로 바꿀 수 없다
    if len(t) < len(s):
        answer = 0
        break
print(answer)
        