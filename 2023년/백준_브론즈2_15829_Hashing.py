'''
    접근법 1
        ord(문자) : 아스키코드
        ord(a) == 97

        chr(숫자)
        chr(97) == 'a'
'''

import sys
input = sys.stdin.readline

# 문자열의 길이
L = int(input())
# 문자열
s = input().rstrip()

answer = 0
for i in range(L):
    answer += (ord(s[i]) - 96) * (31**i)

print(answer%1234567891)