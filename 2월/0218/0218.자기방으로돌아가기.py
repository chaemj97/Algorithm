import sys
sys.stdin = open('sample_input.자기방.txt')

# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # 돌아가야 할 학생들의 수
    N = int(input())
    # A[][0] : 현재방,  A[][1] : 돌아갈 방
    A = [list(map(int,input().split())) for _ in range(N)]

    # 방 번호
    room = [i for i in range(1,401)]

    # 나의 방 번호 사이에 내 뒷사람의 방 번호 중 하나라도 들어 가면 같이 못 움직이니 냅두고
    # 안 들어가면 같이 움직일 수 있으니 삭제
    # 반복
    # 리스트에 남은 학생 수 = 필요한 시간
    j = 0
    while j < len(A)-1:
        k = 1
        while j+k < len(A):
            if (A[j+k][0] not in room[A[j][0]-1:A[j][1]]) and (A[j+k][1] not in room[A[j][0]-1:A[j][1]]):
                A.pop(j+k)
            else:
                k += 1
        j += 1
    result = len(A)

    print(f'#{tc} {result}')