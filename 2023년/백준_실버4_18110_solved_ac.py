'''
    접근법
        round -> 오답
        우리가 알고 있는 반올림 형태인 4사 5입(4 이하는 버리고 5 이상부터 반올림)이 아니라 5사 5입(ROUND_HALF_EVEN or round_to_nearest_even: 앞자리가 홀수면 올리고 앞자리가 짝수면 버리는 방법)을 기반으로 실행
    
'''
import sys
input = sys.stdin.readline

def new_round(x):
    if x - int(x) >= 0.5:
        return int(x)+1
    else:
        return int(x)
    
n = int(input())
if n:
    difficulty = list(int(input()) for _ in range(n))
    difficulty.sort()
    # 15% 
    a = new_round(n*0.15)
    if a:
        difficulty = difficulty[a:-a]
    print(new_round(sum(difficulty)/len(difficulty)))
else:
    print(0)