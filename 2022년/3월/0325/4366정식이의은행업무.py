def check():
    for i in range(len(num2)):
        # 1비트 값만 바꿔서 10진수 값으로 변환
        num2[i] = (num2[i] + 1) % 2
        # 2진수 -> 10진수
        dec = 0
        for idx in range(len(num2)):
            dec = dec*2 + num2[idx]
        result = dec

        # 10진수 -> 3진수
        s = []
        while dec > 0:
            s.append(dec%3)
            dec //= 3
        s = s[::-1]

        # 1개만 다른가?
        cnt = 0
        for idx in range(min(len(num3),len(s))):
            if num3[idx] != s[idx]:
                cnt += 1
        # 둘의 길이가 다르면
        cnt += abs(len(num3)-len(s))
        if cnt == 1:
            return result
        # 되돌리기
        num2[i] = (num2[i] + 1) % 2


# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # 정식이가 기억하는 2진수 표현
    num2 = list(map(int,input()))
    # 3진수 표현
    num3 = list(map(int,input()))
    ans = check()
    print(f'#{tc} {ans}')
