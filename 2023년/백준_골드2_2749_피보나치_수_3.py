'''
    접근법
        피사노 주기를 통해 1,000,000으로 나눈 피보나치 수열의 반복되는 주기는 1,500,000
    
'''
import sys
input = sys.stdin.readline

n = int(input())

# 주기
p = 1500000
fibo = [0,1]

for i in range(2,p):
    fibo.append(fibo[i-2]+fibo[i-1])
    fibo[i] %= 1000000

print(fibo[n%p])