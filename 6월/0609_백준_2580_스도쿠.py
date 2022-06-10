from collections import deque
sudoku = [list(map(int,input().split())) for _ in range(9)]

# 가로 확인-> 세로 확인-> 3*3확인 : 실패....

# 가로, 세로, 3*3 동시에 확인?

# 0 찾기
zero = deque()
for r in range(9):
    for c in range(9):
        if sudoku[r][c] == 0:
            zero.append((r,c))

while zero:
    num = [i for i in range(1,10)]
    r,c = zero[0]
    # 가로 세로 확인
    for n in range(9):
        if sudoku[r][n] in num:
            num.remove(sudoku[r][n])
        if sudoku[n][c] in num:
            num.remove(sudoku[n][c])
    # 3*3 확인
    x=r//3
    y=c//3
    for i in range(x*3,(x+1)*3):
        for j in range(y*3,(y+1)*3):
            if sudoku[i][j] in num:
                num.remove(sudoku[i][j])
    
    if len(num) == 1:
        sudoku[r][c] = num[0]
        zero.popleft()
    else:
        zero.rotate(-1)

for p in sudoku:
    print(*p)