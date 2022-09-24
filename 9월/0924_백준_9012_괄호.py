# 테스트 케이스
T = int(input())

def check(string):
    stack = []
    for i in string:
        # 여는 괄호
        if i == '(':
            stack.append(i)
        # 닫는 괄호
        else:
            # 앞에 여는 괄호가 남아야함
            if stack:
                stack.pop()
            else:
                print('NO')
                return
    # 다 끝났는데 여는 괄호가 남았으면 안됨
    if stack:
        print('NO')
    else:
        print('YES')

for tc in range(1,T+1):
    string = list(input())
    check(string)
    