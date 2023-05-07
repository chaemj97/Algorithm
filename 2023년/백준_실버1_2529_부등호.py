'''
    접근법 
        완전 탐색
    
'''
import sys
input = sys.stdin.readline

k = int(input())
arr = list(input().split())

answer = []

def check(i,num):
    # 숫자를 다 넣었다.
    if i == k:
        answer.append(num)
        return
    
    for n in range(10):
        # 사용한 적 없는 숫자
        if str(n) not in num:
            if arr[i] == '<':
                if int(num[-1]) < n:
                    check(i+1,num+str(n))
            else:
                if int(num[-1]) > n:
                    check(i+1,num+str(n))
for j in range(10):
    check(0,str(j))

answer.sort()
print(answer[-1])
print(answer[0])