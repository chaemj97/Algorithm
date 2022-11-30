# # 수식 문자열
# # 2+3*4/5 -> 2345/*+
#
# # 수식문자열
# N = input()
#
# stack = []
# operator = ['+', '-', '*', '/']
# for i in N:
#     # 피연산자는 바로 출력
#     if i not in operator:
#         print(i,end='')
#     # 연산자는 스택에 push하여 수식이 끝나면 스택에 남아있는 연산자를 모두 pop
#     else:
#         stack.append(i)
# print(''.join(stack[::-1]))

# 후위 표기법
# 2+3*4/5
# 우선순위 : 3 2 1 0
# in-stack priority
isp = {'*':2, '/':2, '+':1, '-':1, '(':0}
# in-coming priority
icp = {'*':2, '/':2, '+':1, '-':1, '(':3}

# 중위 표기식의 토큰을 하나씩 읽어오기
data = '2+3*4/5'
stack = []
for i in range(len(data)):
    # 1. 피연산자는 그냥 출력
    if data[i] in '0123456789':
        print(data[i],end='')
    # 2. 연산자는 우선순위에 따라서 stack에 push하거나
    # pop하고 나서 push
    elif data[i] in '*/+-(':
        # 스택이 비어있으면
        if not stack:
            stack.append(data[i])
        # 스택이 비어있지 않으면
        else:
            if isp[stack[-1]] >= icp[data[i]]:
                # stack이 비어있지 않고 들어가는 연산자보다 우선순위가 크거나 같으면 pop
                while stack and isp[stack[-1]] >= icp[data[i]]:
                    print(stack.pop(),end='')
                # pop하고 나서 push
            stack.append(data[i])
    # 3. 닫는 괄호는 여는 달호가 나올때 까지 pop
    else:
        while stack[-1] != '(':
            print(stack.pop(),end='')
        stack.pop()
# 남아있는 연산자 모두 출력
while stack:
    print(stack.pop(),end='')
print()