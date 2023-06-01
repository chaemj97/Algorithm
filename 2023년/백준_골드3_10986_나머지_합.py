'''
    접근법
    num = [1,2,3,1,2]

    누적합 = [1,3,6,7,9]

    reminder_m(누적합 m으로 나누기) = [1,0,0,1,0]

    reminder = Counter({0: 3, 1: 2})

    1. 누적합 중 m으로 나누어 떨어지는 구간
        1. reminder[0]
    2. 부분 구간 합 중 m으로 나누어 떨어지는 구간
        1. reminder_m에서 값이 같은 거 2개 뽑기
        
        ex) reminder_m[0], reminder_m[3] 은 나머지가 1로 같다
        
        num[0:3] = [1,2,3] 로 해당 구간의 합은 m으로 나누어 떨어진다.
    
'''
from itertools import accumulate
from collections import Counter
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
num = list(map(int,input().split()))
# 누적합 구한 뒤 m으로 나눈 나머지
reminder = Counter(i%m for i in accumulate(num))
print(reminder)
# 처음부터 누적합 중 m으로 나누어 떨어지는 구간
answer = reminder[0]

# 부분 구간 합 중 m으로 나누어 떨어지는 구간 구하기
for i in reminder.values():
    # 나머지가 같은 2개의 값 사이 구간
    answer += (i*(i-1)//2)
    
print(answer)