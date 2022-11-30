def touch(W,cnt):


# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # 터치 가능한 숫자들의 개수, 터치 가능한 연산자들의 개수, 최대 터치 가능한 횟수
    N, O, M = map(int,input().split())
    # 터치 가능한 숫자
    num = list(map(int,input().split()))
    # 터치 가능한 연산자
    oper_key = {1:'+',2:'-',3:'*',4:'//'}
    oper = list(map(int,input().split()))
    # 원하는 숫자
    W = int(input())
    touch(W,0)
    print(f'#{tc}')