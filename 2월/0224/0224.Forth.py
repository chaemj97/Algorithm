import sys
sys.stdin = open('sample_input.Forth.txt')

def Forth(arr):
    stack = []
    for i in arr:

        # 숫자면 스택에 넣기
        if i not in '+-*/.':
            stack.append(int(i))

        # 연산자면 스택에 숫자 2개 꺼내 계싼하고 결과를 다시 스택에 넣기
        elif i in '+-*/':
            # 계산할 숫자가 있어야 함
            if len(stack) >= 2:
                if i == '+':
                    stack[-2] = stack[-2] + stack[-1]
                elif i == '-':
                    stack[-2] = stack[-2] - stack[-1]
                elif i == '*':
                    stack[-2] = stack[-2] * stack[-1]
                elif i == '/':
                    # 나누는 수가 0이면 안됨
                    if stack[-1]:
                        stack[-2] = stack[-2] // stack[-1]
                    else:
                        return 'error'
                stack.pop()
            # 형식이 잘못된 경우 (계산할 숫자 없는데 연산자 나오는 경우)
            else:
                return 'error'

        # '.'
        elif i == '.':
            # 계산이 끝난 경우
            if len(stack) == 1:
                return stack[0]
            # 계산할 숫자가 남아있으면
            else:
                return 'error'

# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # 연산 코드
    arr = list(input().split())

    print(f'#{tc} {Forth(arr)}')

