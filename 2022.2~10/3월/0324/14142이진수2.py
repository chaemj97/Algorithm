T = int(input()) # 테스트 케이스의 수
for tc in range(1,T+1):
    N = float(input())
    a = 1 # 지수
    result = ''
    while N >0:
        result += str(int(N//2**-a))
        N %=2**(-a)
        a += 1
    if len(result) > 13:
        result = 'overflow'
    print(f'#{tc} {result}')