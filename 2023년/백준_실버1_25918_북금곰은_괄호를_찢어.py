'''
    접근법
        여는 괄호 +1
        닫는 괄호 -1
'''
import sys
input = sys.stdin.readline

# 문자의 길이
n = int(input())
# 목표 문자
s = input().rstrip()

# 괄호의 개수가 맞지 않는 경우 -> 실패
if s.count('(') != s.count(')'):
    print(-1)
    sys.exit()

answer = 0
cnt = 0
for i in s:
    # 여는 괄호
    if i == '(':
        cnt += 1
    # 닫는 괄호
    else:
        cnt -= 1
    
    answer = max(answer,abs(cnt))

# 여는 괄호와 닫는 괄호의 짝이 맞다
if cnt == 0:
    print(answer)
# 짝이 맞지 않다
else:
    print(-1)