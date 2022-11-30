# 2xy+x+y 
# = x(2y+1)+0.5(2y+1)-0.5 
# = (x+0.5)(2y+1)-0.5
# = 0.5(2x+1)(2y+1)-0.5
# = 0.5{(2x+1)(2y+1)-1}
# = 0.5{홀수*홀수-1}

# 2배 한 후 +1이 소수라면 꽝


# 아직 불가능.....
from sys import stdin
input = stdin.readline

# 소수 판별 함수
def is_prime_number(num, a):
    # 3. num-1을 (2^s)*d 형태로 바꾼다.
    d = num -1
    s = 0
    while d%2 == 0:
        s += 1
        d //= 2
    # 4. 
    


# 아파트의 면적의 수
N = int(input())
cnt = 0
# 아파트 면적
for _ in range(N):
    area = int(input())
    x = area*2+1
    # 1. 2,3,5,7,11을 선택
    check = 0
    for i in [2,3,5,7,11]:
        # 2. x가 소수인가 검사
        if is_prime_number(x,i):
            check += 1
        else:
            break
    # x가 소수인가 확인
    if check == 5:
        cnt += 1
print(cnt)

