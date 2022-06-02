# https://chaemi720.tistory.com/143

from itertools import permutations

# 현 우선순위에 따라 연산하기
def money(prior, oper, num):
    for p in prior:
        while p in oper:
            i = oper.index(p)
            num[i] = str(eval(num[i] + p + num[i + 1]))
            num.pop(i + 1)
            oper.pop(i)
    return num[0]


def solution(expression):
    # 계산할려면 리스트여야 할듯
    num = []
    oper = []
    start = 0
    for idx, i in enumerate(expression):
        if i in ['+', '*', '-']:
            # 피연산자
            num += [expression[start:idx]]
            # 연산자
            oper += [i]
            start = idx + 1
    # 마지막 남은 피연산자
    num += [expression[start:]]

    # 중복 삭제
    oper1 = list(set(oper))

    max_money = 0

    # 우선순위
    for prior in list(permutations(oper1, len(oper1))):
        numbers = num.copy()
        operator = oper.copy()

        # 연산
        result = money(prior, operator, numbers)

        # 최대값인지 확인
        if max_money < abs(int(result)):
            max_money = abs(int(result))

    return max_money