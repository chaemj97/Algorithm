# 테스트 케이스 수
T = int(input())
for tc in range(1,T+1):
    # N : 노드의 개수, M : 리프 노드의 개수, L : 값을 출력할 노드 번호
    N,M,L = map(int,input().split())

    tree = [0]*(N+1)
    # M개 줄에 리프노드 번호, 값
    for i in range(M):
        leap_num, value = map(int,input().split())
        tree[leap_num] = value

    for k in range(N,0,-1):
        tree[k//2] += tree[k]
    # # 마지막꺼만 오른쪽 자식 있는지 확인하면 될 듯
    # # 마지막자식의 부모 빼고는 다 자식 2명
    # if N%2: # 마지막자식은 부모의 오른쪽 자식
    #     tree[N//2] = tree[N]+ tree[N-1]
    #     N -= 2
    # else:
    #     tree[N//2] = tree[N]
    #     N -= 1
    # for j in range(N,1,-2):
    #     # 모드 자식 2명
    #     tree[j//2] = tree[j]+tree[j-1]

    print(f'#{tc} {tree[L]}')

