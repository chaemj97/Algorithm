from sys import stdin

def lookForNumList(r,c):
    nums = [0] * 10
    for i in range(9):
        nums[sudoku[i][c]] = 1
        nums[sudoku[r][i]] = 1
    for s in range(r//3*3, r // 3 * 3 + 3):
        for t in range(c // 3 * 3, c // 3 * 3 + 3):
            nums[sudoku[s][t]] = 1
    return nums

def sudokuSolve(idx):
    global success
    if idx == len(zero):
        success = True
        for row in sudoku:
            print(*row)
        return
        
    r,c = zero[idx]
    if not sudoku[r][c]:
        nums = lookForNumList(r,c)
        for i in range(1,len(nums)):
            if not nums[i]:
                sudoku[r][c] = i
                sudokuSolve(idx+1)
                if not success:
                    sudoku[r][c] = 0

sudoku = [list(map(int,stdin.readline().split())) for _ in range(9)]
zero = [(r,c) for r in range(9) for c in range(9) if sudoku[r][c] == 0]
success = False

sudokuSolve(0)