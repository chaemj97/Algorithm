

from sys import stdin,maxsize
input = stdin.readline
INF = maxsize

# N이 19이하 -> 완탐
# 수식의 길이
N = int(input())

# 수식
arr = list(input())
# 피연산자
num = []
# 연산자
oper = []
# 연산자, 피연산자 구분
for i in range(N):
    if i%2:
        oper.append(arr[i])
    else:
        num.append(arr[i])

max_result = -INF

# 괄호 넣기
def insert(idx,result):
    global max_result

    # 연산 끝
    if idx == len(oper):
        # 최대 구하기
        max_result = max(max_result,int(result))
        return

    # 첫번째 연산자가 괄호 안
    first = str(eval(result + oper[idx] + num[idx+1]))
    insert(idx+1,first)

    # 2번째 연산자가 괄호 안 (식의 연산자가 1개 남았을 때 불가능)
    if idx + 1 < len(oper):
        second = str(eval(num[idx+1] + oper[idx+1] + num[idx+2]))
        second = str(eval(result + oper[idx] + second))
        insert(idx+2,second)

insert(0,num[0])

print(max_result)