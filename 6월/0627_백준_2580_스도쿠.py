# https://chaemi720.tistory.com/187

from sys import stdin

def lookForNumList(r,c):
    nums = [0] * 10
    # 이 위치에 들어갈 수 없는 숫자 인덱스에 1 체크
    for i in range(9):
        nums[sudoku[i][c]] = 1
        nums[sudoku[r][i]] = 1
    for s in range(r//3*3, r // 3 * 3 + 3):
        for t in range(c // 3 * 3, c // 3 * 3 + 3):
            nums[sudoku[s][t]] = 1
    return nums

# 스도쿠 풀기
def sudokuSolve(idx):
    global success
    # 스도쿠 다 풀었는가?
    if idx == len(zero):
        success = True
        for row in sudoku:
            print(*row)
        return

    # 지금 풀 스도쿠 부분(r,c)
    r,c = zero[idx]
    if not sudoku[r][c]:
        # 이 자리에 들어갈 수 있는 숫자 모임
        nums = lookForNumList(r,c)
        # 스도쿠 숫자 넣기
        for i in range(1,10):
            if not nums[i]:
                sudoku[r][c] = i
                sudokuSolve(idx+1)
                # (r,c)위치에 i 넣었더니 스도쿠 해결이 안된다?
                if not success:
                    # 초기화
                    sudoku[r][c] = 0

# 스도쿠 문제
sudoku = [list(map(int,stdin.readline().split())) for _ in range(9)]
# 스도쿠 풀어야 하는 부분 모임
zero = [(r,c) for r in range(9) for c in range(9) if sudoku[r][c] == 0]
success = False

sudokuSolve(0)