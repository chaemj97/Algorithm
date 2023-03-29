'''
# pow(a,b) = a^b

# 1~10^18중 세제곱
pow_3 = []
for i in range(10**6+1):
    pow_3.append(pow(i,3))

# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # N이 pow_3함수 안에 있으면 인덱스 출력
    # 없으면 -1 출력력
    try:
        print(f'#{tc} {pow_3.index(N)}')
    except:
        print(f'#{tc} {-1}')
'''

import math
T = int(input())
for tc in range(1, T+1):
    num = int(input())
    # 세제곱근
    result = num**(1/3)
    # 반올림
    v = round(result)
    # 세제곱근이 정수이면 반올림해도 같은 값
    if math.isclose(result, v):
        print(f'#{tc} {int(v)}')
    else:
        print(f'#{tc} -1')
