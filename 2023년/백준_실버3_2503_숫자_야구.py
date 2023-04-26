'''
    접근법 1
        목표 : 가능성이 있는 답의 총 개수
        
        정답이 될 수 있는 모든 후보와 test 비교하기
            -> strike의 수와 ball의 수가 같으면 남기기
 
        
'''
from itertools import permutations
import sys
input = sys.stdin.readline

# 질문 횟수
n = int(input())
# 숫자 야구에 나올 수 있는 모든 수
candidate = list(permutations([1,2,3,4,5,6,7,8,9],3))

def check(num1, num2, a, b):
    # 스트라이크 수
    strike = [c1 == c2 for c1, c2 in zip(num1, num2)]
    # 볼의 수 구하기
    # 스트라이크가 아닌 위치의 숫자 중 겹치는 숫자가 있으면 볼
    num1 = set(c for i, c in enumerate(num1) if not strike[i])
    num2 = set(c for i, c in enumerate(num2) if not strike[i])
    return a == sum(strike) and b == len(num1 & num2)


for _ in range(n):
    test, s, b = map(int,input().split())
    test = list(map(int,str(test)))
    # test의 strike수와 ball의 수가 일치하는 후보만 남기기
    candidate = [candi for candi in candidate if check(test, candi, s, b)]

print(len(candidate))