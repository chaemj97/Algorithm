def pattern(s):
    j = 1
    length = 1
    while j < len(s):
        # 덩어리로 비교
        if s[0:length] == s[j:j+length]:
            length += 1
            # 패턴 마디라면 다음구간도 같아야함
            if s[0:length] == s[j+length:j+length+length]:
                return length
        else:
            j += 1

# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    s = list(input())

    print(f'#{tc} {pattern(s)}')


