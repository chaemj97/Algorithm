# https://chaemi720.tistory.com/164

# board : 인형배치(아래에서 위로 쌓임), moves : 인형 뽑는 열 위치

def solution(board, moves):
    # 인형 터트린 수
    answer = 0
    N = len(board)
    # 인형 바구니
    dolls = []

    # 인형배치(왼쪽에서 오른쪽으로 쌓기)
    board = list(map(list, zip(*board[::-1])))

    # 인형 없는 부분 지우기
    for i in range(N):
        while 0 in board[i]:
            board[i].remove(0)

    for n in moves:
        # 인형이 존재할 때
        if board[n - 1]:
            doll = board[n - 1].pop()
            # 바구니에 인형 없거나 마지막에 넣은 인형과 다르다면
            if dolls == [] or doll != dolls[-1]:
                # 바구니에 추가
                dolls.append(doll)
            # 마지막에 넣은 인형과 같으면
            else:
                # 터트리기
                dolls.pop()
                answer += 2

    return answer