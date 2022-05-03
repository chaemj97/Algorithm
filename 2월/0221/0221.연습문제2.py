# 괄호의 짝을 검사하는 프로그램
def check(data):
    stack = []
    for i in data:
        # 여는 괄호면 스택 push
        if i == '(':
            stack.append(i)
        # 닫는 괄호면 스택 pop
        else:
            # 여는 괄호가 먼저 나왔으면
            if stack:
                stack.pop()
            # 스택이 비어있으면  -> 짝이 맞지 않아 실패
            else:
                return False
    # 모두 검사했는데 여는 괄호가 남아있다면 - > 짝이 맞지 않아 실패
    if stack:
        return False
    return True

data1 = '()()((()))'
print(check(data1))
data2 = '((()(()))'
print(check(data2))