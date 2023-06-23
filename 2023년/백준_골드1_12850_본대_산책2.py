'''
    접근법
        정보과학관을 시작으로 반시계방향으로 인덱스 부여
        정보과학관, 전산관, 신양관, 진리관, 학생회관, 형남공학관, 한경직기념관, 미래관
        arr = [
                [0, 1, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 1],
                [0, 1, 0, 1, 0, 0, 1, 1],
                [0, 0, 1, 0, 1, 0, 1, 0],
                [0, 0, 0, 1, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0, 1, 0],
                [0, 0, 1, 1, 0, 1, 0, 1],
                [1, 1, 1, 0, 0, 0, 1, 0],
            ]
        
        # 인접 행렬
        arr x arr == arr2
        arr2[i][j] : i에서 j로 2번만에 갈 수 있는 경우의 수
        arr3[i][j] : i에서 j로 3번만에 갈 수 있는 경우의 수
'''
import sys
input = sys.stdin.readline

# 산책 시간
d = int(input())

# 연결 
arr = [
        [0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 1, 1],
        [0, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 0, 0, 1, 0],
    ]

# 0번에서 산책 후 0번까지 오는데 시간 d분
# arrd[0][0] 구하기

# 행렬 곱
def matrix_multiply(A,B):
    # 계산 결과
    # A x B = result
    result = [[0]*8 for _ in range(8)]
    # result[i][j] = A[i][0]*B[0][j] + A[i][1]*B[1][j] + ... + A[i][7]*B[7][j]
    for i in range(8):
        for j in range(8):
            # result[i][j] 구하기
            for k in range(8):
                result[i][j] += A[i][k]*B[k][j]
            result[i][j] %= 1000000007
    return result

# arr행렬 d번 곱하기
# A^n 구하기
def cal_D(A,n):
    if n == 1:
        return A
    # ex) n = 10 -> A^10 = A^5 * A^5
    # ex) n = 11 -> A^11 = A^10 * A = (A^5 * A^5) * A
    # 공통으로 A^5가 필요
    half_A = cal_D(A,n//2)
    
    # n이 짝수인 경우
    if n%2 == 0:
        return matrix_multiply(half_A,half_A)
    # n이 홀수인 경우
    else:
        return matrix_multiply(matrix_multiply(half_A,half_A),A)
    
# 0번에서 산책 후 0번까지 오는데 시간 d분
# == arr d번 곱한 후 (0,0) 구하기
print(cal_D(arr,d)[0][0])