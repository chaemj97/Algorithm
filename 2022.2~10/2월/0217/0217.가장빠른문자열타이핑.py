# import sys
# sys.stdin = open('sample_input.가장빠른.txt')
# T : 테스트 케이스 수
T = int(input())
for tc in range(1,T+1):
    A, B = map(str,input().split())
    # 타이핑 수 : len(A)-(B가 A에 속한 횟수)*(len(B)-1)
    # cnt = (B가 A에 속한 횟수)
    cnt = 0
    # A의 인덱스 (비교 위치)
    i = 0
    while i <= len(A)-len(B):
        # 속한다면 - > 속한 횟수 +1, 비교위치 +len(B)
        if A[i:i+len(B)] == B:
            cnt += 1
            i += len(B)
        # 속하지 않는다면 - > 비교위치 +1
        else:
            i += 1
    result = len(A) - cnt * (len(B)-1)

    print(f'#{tc} {result}')

