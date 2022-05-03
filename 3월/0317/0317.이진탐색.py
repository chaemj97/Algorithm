# 완전 이진 트리 만들기 : in_order
def in_order(n):
    global value
    if n <= N:
        in_order(n*2)
        tree[n] = value
        value += 1
        in_order((n*2+1))

# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    tree = [0]*(N+1)
    value = 1

    in_order(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')
