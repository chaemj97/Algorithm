def fun(arr):
    stack = ['']*len(arr)
    # '(', ')', '{' ,'}'
    top = -1
    for i in arr:
        # (,{ 여는 괄호이면 stack에 집어넣기
        if i == '(' or i == '{':
            top += 1
            stack[top] = i

        # 닫는 괄호
        # ')'면 마지막에 넣은 여는 괄호가 '('여야 성공, 아니면 실패
        elif i == ')':
            if stack[top] == '(':
                top -= 1
            else:
                return 0
        # '}'면 마지막에 넣은 여는 괄호가 '{'여야 성공, 아니면 실패
        elif i == '}':
            if stack[top] == '{':
                top -= 1
            else:
                return 0
    # 여는 괄호, 닫는 괄호 짝이 다 맞다면 (stack에 남은 여는 괄호가 없다면) 성공
    if top == -1:
        return 1
    else:
        return 0


# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # 테스트 케이스
    C = input()

    result = fun(C)

    print(f'#{tc} {result}')

# # 교수님
def solve(data):
    # 여는 괄호면 stack에 push
    # 닫는 괄호면 stack에서 pop 해서 그 결과와 짝이 맞는지 검사
    # 짝이 맞지 않으면 False
    # 모든 데이터를 다 읽었을 때, stack이 비어있지 않으면 False
    # 비어있으면 True
    N = len(data)

    bracket_lst = ['{','(',')','}']

    stack =[]
    for i in range(N):
        # 괄호인가?
        if data[i] in bracket_lst:
            # 여는 괄호면 stack에 추가
            if data[i] == '{' or data[i] == '(':
                stack.append(data[i])
            # 닫는 괄호
            else:
                # 닫는 괄호가 먼저 나옴, 짝이 없음
                if not stack:
                    return 0

                # 가장 마지막 여는 괄호
                top = stack.pop()
                # 짝꿍 안맞음
                if data[i] == ')' and top != '(':
                    return 0
                if data[i] == '}' and top != '{':
                    return 0
    # 반복 마친 후 여는 괄호 남으면 짝 안 맞음
    if stack:
        return 0
    return 1

