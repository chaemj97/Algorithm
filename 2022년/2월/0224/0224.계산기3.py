import sys
sys.stdin = open('input.계산기3.txt')

# 테스트 케이스 개수
T = 10
for tc in range(1,T+1):
    # 테스트 케이스의 길이
    N = int(input())
    # 테스트 케이스
    TC = list(input())

    # in-stack priority
    isp = {'*':2, '+':1, '(':0}
    # in-coming priority
    icp = {'*':2, '+':1, '(':3}

    # 1. 후위 표기식으로 바꾸기
    result_ls = []
    stack = []
    for i in TC:
        # 숫자면 결과에 넣기
        if i in '0123456789':
            result_ls.append(i)
        # '*' or '+' or '('
        elif i in '*+(':
            # 스택이 비어있으면
            if not stack:
                stack.append(i)
            # 스택이 비어있지 않으면
            else:
                # stack[-1] 보다 우선순위가 낮다면 stack에 있는 연산자 다 빼내기
                if isp[stack[-1]] >= icp[i]:
                    while stack and isp[stack[-1]] >= icp[i]:
                        result_ls.append(stack.pop())
                stack.append(i)
        # ')'
        else:
            while stack[-1] != '(':
                result_ls.append(stack.pop())
            stack.pop()
    # 남아있는 연산자 모두 넣기
    while stack:
        result_ls.append(stack.pop())

    # 2. 계산하기
    result = []
    i = 0
    for i in result_ls:
        if i != '*' and i != '+':
            result.append(i)
        elif i == '+':
            result[-2] = int(result[-2]) + int(result[-1])
            result.pop()
        else:
            result[-2] = int(result[-2]) * int(result[-1])
            result.pop()

    print(f'#{tc} {result[0]}')