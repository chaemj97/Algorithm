'''
    접근법
    0: ZERO -> Z
    1: ONE -> O
    2: TWO -> W
    3: THREE -> T
    4: FOUR -> U
    5: FIVE -> F
    6: SIX -> X
    7: SEVEN -> S
    8: EIGHT -> G
    9: NINE -> I
    
'''
from collections import Counter
import sys
input = sys.stdin.readline

# 각 숫자 단어가 가지고 있는 대표 문자 dictionary
num = {'Z':'ZERO0','W':'TWO2','U':'FOUR4','X':'SIX6','G':'EIGHT8',
       'F':'FIVE5','T':'THREE3','O':'ONE1','S':'SEVEN7','I':'NINE9'}

T = int(input())
for t in range(1,T+1):
    s = list(input().rstrip())
    # 각 알파벳 개수 
    cnt = Counter(s)
    answer = ''
    
    for k,v in num.items():
        # 문자 k가 존재하면 숫자 v[-1]이 존재
        if cnt[k] > 0:
            # 숫자 v[-1]가 c개 존재
            c = cnt[k]
            answer += v[-1]*c
            # 숫자 v[-1]에 들어가는 알파벳 c개만큼씩 빼기
            for i in v[:-1]:
                cnt[i] -= 1*c
                
    answer = ''.join(sorted(answer))
    print(f'Case #{t}: {answer}')