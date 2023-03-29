# 테스트 케이스의 수
T = int(input())
for tc in range(1,T+1):
    # N자리 16진수
    N, num16 = input().split()
    print(f'#{tc}',end=' ')
    for i in range(int(N)):
        # 16진수 -> 10진수
        num10 = int(num16[i],16)
        # 10진수 -> 2진수
        # 4자리 채우기
        print(format(num10,'b').zfill(4),end='')
    print()

T = int(input())
for tc in range(1, 1 + T):
    N, data = input().split()
    result = ''
    for i in range(int(N)):
        if data[i] in '0123456789':
            num = int(data[i])
        else:
            num = ord(data[i]) - ord('A') + 10

        for j in range(3, -1, -1):
            result += "1" if num & (1 << j) else "0"

    print(f'#{tc} {result}')