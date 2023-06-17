'''
    접근법
        경우를 나눠서 구현하기
        괄호 여러 묶음은 제일 안쪽 괄호일때만 answer 추가
    
'''
import sys
input = sys.stdin.readline

s = list(input().rstrip())

stack = []
answer = 0

temp = 1
for i in range(len(s)):
    a = s[i]
    # 여는 괄호
    if a == '(':
        stack.append(a)
        temp *= 2
    elif a == '[':
        stack.append(a)
        temp *= 3
    
    # 닫는 괄호
    elif a == ')':
        # 스택이 비어있거나 짝이 맞지 않는 경우
        if not stack or stack[-1] == '[':
            answer = 0
            break
        # 괄호를 완성?
        if s[i-1] == '(':
            answer += temp
        temp //= 2
        stack.pop()
        
    elif a == ']':
        # 스택이 비어있거나 짝이 맞지 않는 경우
        if not stack or stack[-1] == '(':
            answer = 0
            break
        # 괄호를 완성?
        if s[i-1] == '[':
            answer += temp
        temp //= 3
        stack.pop()
    
# 스택이 남아있는 경우
if stack:
    print(0)
else:
    print(answer)