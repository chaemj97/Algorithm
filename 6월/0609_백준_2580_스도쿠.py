
sudoku = [list(map(int,input().split())) for _ in range(9)]

# 가로,세로
def sudoku_check(sudoku):
    for r in range(9):
        res = set([i for i in range(1,10)])
        res -= set(sudoku[r])
        if len(res) == 1:
            for c in range(9):
                if sudoku[r][c] == 0:                
                    sudoku[r][c] = list(res)[0]
                    break
# 가로
sudoku_check(sudoku)

# 세로
# 전치
sudoku = list(map(list,zip(*sudoku)))
sudoku_check(sudoku)
sudoku = list(map(list,zip(*sudoku)))
# 3*3
for r in range(0,9,3):
    for c in range(0,9,3):
        res = set([i for i in range(1,10)])
        x,y = -1,-1
        for i in range(r,r+3):
            for j in range(c,c+3):
                if sudoku[i][j] != 0:
                    res -= set([sudoku[i][j]])
                else:
                    x,y = i,j
        if len(res) == 1 and x != -1 and y != -1:
            sudoku[x][y] = list(res)[0]
print()     
for k in sudoku:
    print(*k)

    
        