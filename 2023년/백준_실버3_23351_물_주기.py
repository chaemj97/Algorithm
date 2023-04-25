'''
    접근법 1
        목표 : 첫 캣닢이 죽는 날짜
        
        구현
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# n : 화분의 수
# k : 초기 수분
# a : 연속된 a개의 화분 물 주기
# b : b만큼 물 주기
n,k,a,b = map(int,input().split())
pot = [k]*n
day = 0
def water(i):
    global pot,day
    day += 1
    # 물 주기
    for j in range(a):
        pot[i+j] += b
    # 모든 화분 1 감소
    for k in range(n):
        pot[k] -= 1
        # 캣닢이 죽었는가?
        if pot[k] == 0:
            return
    water((i+a)%n)
    
water(0)
print(day)