# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # N : 상자의 개수, Q : 상자 변경을 반복할 횟수
    N,Q = map(int,input().split())

    # index 수 일치를 위해 리스트 길이 N+1
    result = [0]*(N+1)
    # L~R번의 상자의 해당 값을 i로 변경
    for i in range(1,Q+1):
        L,R = map(int,input().split())
        for j in range(L,R+1):
            result[j] = i

    print(f'#{tc}',*result[1:])
    print(f'#{tc}',' '.join(list(map(str,result[1:]))))
