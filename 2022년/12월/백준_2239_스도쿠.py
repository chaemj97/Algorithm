import sys
input = sys.stdin.readline

sudoku = [list(map(int,input().rstrip())) for _ in range(9)]

# 빈칸 위치
zero = []
for r in range(9):
    for c in range(9):
        if sudoku[r][c] == 0:
            zero.append([r,c])

def check(i):
    # 다 채웠는가?
    if i == len(zero):
        # 결과 출력
        for ii in range(9):
            print("".join(map(str,sudoku[ii])))
        return True

    # 확인할 위치
    cr,cc = zero[i][0],zero[i][1]

    # 전체 수
    total = set([i for i in range(1,10)])
    # 들어갈 수 없는 수
    used = []
    # 가로 세로 확인
    used = sudoku[cr] + [sudoku[a][cc] for a in range(9)]
    # 사각형
    for r in range((cr//3)*3,(cr//3)*3+3):
        for c in range((cc//3)*3,(cc//3)*3+3):
            used.append(sudoku[r][c])
    # 넣어보기
    for num in sorted(total - set(used)):
        sudoku[cr][cc] = num
        if check(i+1):
            return True
        sudoku[cr][cc] = 0
    return False

check(0)
