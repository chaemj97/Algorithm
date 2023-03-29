# 2 + 3 * 4 / 5
# 후위 표기법으로 바꾸기
# 우선순위 : 3 2 1 0
isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}

# 중위표기식의 토크을 하나씩 읽어오기
data = '2+3*4/5'
stack = []
for i in range(len(data)):
    # 1. 피연산자는 그냥 출력
    if data[i] in '0123456789':
        print(data[i], end='')
    # 2. 연산자는 우선순위에 따라서 stack에 push 하거나
    elif data[i] in '*/+-(':
        if not stack:   #스택이 비어있으면
            stack.append(data[i])
        else:   #스택이 비어있지 않으면
            #내가 크면 그냥 들어가면 됩니다.
            if isp[stack[-1]] >= icp[data[i]]:
                while stack and isp[stack[-1]] >= icp[data[i]]:
                    print(stack.pop(),end='')
                # pop하고 나서 push
            stack.append(data[i])
    # 3. 닫는 괄호는 여는 괄호가 나올때 까지 pop
    else:
        while stack[-1] != '(':
            print(stack.pop(),end='')
        stack.pop()
while stack:    # 남아있는 연산자 모두 출력
    print(stack.pop(), end='')

print()
