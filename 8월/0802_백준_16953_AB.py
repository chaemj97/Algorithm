from sys import stdin
input = stdin.readline

# A를 B로 바꾸기
A, B = map(int,input().split())

cnt = 0
while A != B:
    # 만들 수 없는 경우
    if A > B:
        cnt = -2
        break
    b = str(B)
    # 짝수만 나누기 가능
    if b[-1] != '1':
        if B % 2 == 0:
            B //= 2
        else:
            cnt = -2
            break
    else:
        B = int(b[:-1])
    cnt += 1   

print(cnt+1)