'''
    접근법
        stack 구현
    
'''
import sys
input = sys.stdin.readline

s = list(input().rstrip())

answer = ''
stack = []
flag = False
for i in s:
    if i == '<':
        answer += ''.join(stack[::-1])
        stack = []
        flag = True
        answer += i
    elif i == '>':
        answer += i
        flag = False
    
    # 문자    
    elif i.isalpha():
        if flag:
            answer += i
        else:
            stack.append(i)
    # 숫자
    elif i.isdigit():
        stack.append(i)       
    
    # 공백
    else:
        if flag:
            answer += i
        else:
            answer += ''.join(stack[::-1])
            answer += ' '
            stack = []
if stack:
    answer += ''.join(stack[::-1])
print(answer.lstrip()) 
        
        