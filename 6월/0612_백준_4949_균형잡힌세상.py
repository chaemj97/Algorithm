# https://chaemi720.tistory.com/163

from sys import stdin
import re

while True:
    result = 'yes'
    s = stdin.readline().rstrip()
    # 종료조건(맨 마지막에 점 하나)
    if s == '.':
        break
    # 검사!!
    # 숫자 영어 점 공백 제거
    s = re.sub('[0-9a-zA-Z. ]','',s)
    # 괄호가 없는거면 통과!
    if s != '':
        # 괄호 확인
        stack=[]
        for i in s:
            # 여는 괄호면 추가
            if i == '(' or i == '[':
                stack.append(i)
            # 닫는 괄호, 짝이 존재하고 짝이 맞아
            elif i == ')' and stack and stack[-1] == '(':
                stack.pop()
            # 닫는 괄호, 짝이 존재하고 짝이 맞아
            elif i == ']' and stack and stack[-1] == '[':
                stack.pop()
            # 닫는 괄호, 짝이 맞지 않아
            elif i == ')' or i == ']':
                result = 'no'
                break
        # 다 했는데 스택에 남아있다 == 짝이 맞지 않다.
        if stack:
            result = 'no'
    print(result)

                                
