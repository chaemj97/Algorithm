'''
    접근법 1
        식의 결과값을 가장 작게 만들기
        -> - 뒤의 숫자를 크게 만들기
        -> - 기준으로 나누기
        
        ex) 55 - 50 + 40 - 30 + 20 
            = 55 - (50 + 40) - (30 + 20)
'''

import sys
input = sys.stdin.readline

# - 기준으로 식 나누기
expression = input().rstrip().split('-')

num = []
for exp in expression:
    s = 0
    for j in exp.split('+'):
        s += int(j)
    num.append(s)

# 첫번째 수 뒤로는 다 빼기
n = num[0]
for i in range(1,len(num)):
    n -= num[i]
print(n)