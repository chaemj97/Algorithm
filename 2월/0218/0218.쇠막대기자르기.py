# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # 쇠막대기와 레이저 배치
    arr  = input()
    # 잘린 막대기 개수
    result = 0
    # 쌓인 막대기 개수
    cnt = 0
    for i in range(len(arr)):
        # '(' : 막대기 추가
        if arr[i] == '(':
            cnt += 1
        # ')' : 앞이 무엇인지 확인하기
        else:
            cnt -= 1
            # 앞이 '('이면 레이저 -> 앞에 '(' 막대기 개수 추가가 아님
            if arr[i-1] == '(':
                result += cnt
            # 앞이 ')'이면 막대기 끝 -> 자르고 남은 막대기 끝
            else:
                result += 1
    print(f'#{tc} {result}')

