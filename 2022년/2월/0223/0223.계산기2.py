import sys
sys.stdin = open('input.계산기.txt')

for tc in range(1,11):
    # 테스트 케이스의 길이
    T = int(input())
    # 테스트 케이스
    TC = list(input())

    # *는 바로 계산하고 +기다렸다 마지막에 계산
    stack = []
    i = 0
    while i < T:
        # 숫자와 '+'를 stack에 넣기
        if TC[i] != '*':
            # '+'일때 stack안에 이미 '+' 있으면 이전 '+' 계산
            if len(stack) > 1 and stack[-2] == '+':
                stack[-3] = int(stack[-3]) + int(stack[-1])
                # '+'와 더한 숫자 지우기
                stack.pop()
                stack.pop()
            stack.append(TC[i])
            i += 1

        # '*'면 바로 계산
        elif TC[i] == '*':
            stack[-1] = int(stack[-1]) * int(TC[i + 1])
            i += 2

    # 다 넣고 나면 a + b 형태로 3개가 남음
    # 마지막 연산
    result = int(stack[0]) + int(stack[2])

    print(f'#{tc} {result}')



