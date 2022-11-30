# value 가 단조이면 True, 아니면 False
def check(value):
    strV = str(value)
    for i in range(1,len(strV)):
        if strV[i-1] > strV[i]:
            return False
    return True

# 테스트 케이스의 수
T = int(input())
for tc in range(1,T+1):
    # 정수 개수
    N = int(input())
    A = list(map(int,input().split()))

    maxV = -1
    for i in range(1,N):
        for j in range(i+1,N):
            value = A[i] * A[j]
            if check(value):
                if maxV < value:
                    maxV = value


    print(f'#{tc} {maxV}')