'''
    접근법
    
'''
import sys
input = sys.stdin.readline

n = int(input())
l = len(str(n))
answer = 0

for i in range(l-1):
    answer += 9*10**i*(i+1)

answer += (n - 10**(l-1)+1)*l
print(answer)