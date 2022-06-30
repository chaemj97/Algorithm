# https://chaemi720.tistory.com/195

def solution(m, n, board):

    # 위에서 떨어지는게 아니라 오른쪽에서 왼쪽으로 떨어지도록 돌리기
    board = list(map(list,zip(*board[::-1])))
    poppop_count = 0
    # 터트릴게 없을 때까지
    while True:
        # 이번 turn에 터트린 위치 set
        poppop = set()
        for r in range(n-1):
            for c in range(m-1):
                # 2x2 형태로 4개가 같다면 (터트린 위치의 값은 0)
                if board[r][c] == board[r+1][c] == board[r+1][c+1] == board[r][c+1] != 0:
                    # 집합 더하는 방법 set |= set
                    poppop |= set([(r,c),(r+1,c),(r+1,c+1),(r,c+1)])
        
        # 터트리고 칸 채우기
        for i,j in poppop:
            board[i][j] = 0

        for r in range(n):
            zero = []
            nonzero = []
            for c in range(m):
                if board[r][c] == 0:
                    zero += [0]
                else:
                    nonzero += board[r][c]
            board[r] = nonzero + zero

        # 이번 turn에 터트린게 없으면 끝내기
        if len(poppop) == 0:
            break
        # 터트린 블록 수 더하기
        poppop_count += len(poppop)
        
    return poppop_count