'''
    접근법
        3줄씩 반복을 이용
    
'''
import sys
input = sys.stdin.readline

n = int(input())

def star(n):
    # n이 3일때
    if n == 3:
        return ['***','* *','***']

    # n이 3보다 클 때
    stars = star(n//3)
    result = []
    # 첫번째 
    for s in stars:
        result.append(s*3)
    # 두번째
    for s in stars:
        result.append(s + ' '*(n//3) + s)
    # 세번째
    for s in stars:
        result.append(s*3)
    
    return result

# 결과 출력
answer = star(n)
for i in range(n):
    print(''.join(answer[i]))