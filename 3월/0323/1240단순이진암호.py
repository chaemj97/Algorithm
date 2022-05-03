num = {'0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011' : 4,
        '0110001' : 5,'0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}
import sys
sys.stdin = open('input.단순2진.txt')

# 테스트 케이스의 수
T = int(input())
for tc in range(1,T+1):
    # 배열의 세로 크기 N, 배열의 가로 크기 M
    N,M = map(int,input().split())
    # 암호코드 받기 1이 있는 1줄만 받으면 됨
    arr = [input() for _ in range(N)]
    for i in range(N):
        if '1' in arr[i]:
            code = arr[i]
            break
    # 암호코드 잘라읽기
    for j in range(M-1,-1,-1):
        if code[j] == '1':
            k = j
            break
    secret_code = []
    for s in range(k-55,k+1,7):
        secret_code.append(num[code[s:s+7]])
    # 코드 정상인가?
    check = 0
    for a in range(4):
        check += secret_code[a*2]*3 + secret_code[a*2+1]
    if not check%10:
        print(f'#{tc} {sum(secret_code)}')
    else:
        print(f'#{tc} {0}')

