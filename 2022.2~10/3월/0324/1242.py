hex = [
    [0, 0, 0, 0],  # 0
    [0, 0, 0, 1],  # 1
    [0, 0, 1, 0],  # 2
    [0, 0, 1, 1],  # 3
    [0, 1, 0, 0],  # 4
    [0, 1, 0, 1],  # 5
    [0, 1, 1, 0],  # 6
    [0, 1, 1, 1],  # 7
    [1, 0, 0, 0],  # 8
    [1, 0, 0, 1],  # 9
    [1, 0, 1, 0],  # A
    [1, 0, 1, 1],  # B
    [1, 1, 0, 0],  # C
    [1, 1, 0, 1],  # D
    [1, 1, 1, 0],  # E
    [1, 1, 1, 1]  # F
]

scode = [[[0]*5 for _ in range(5)] for _ in range(5)]
print(scode)
scode[2][1][1] = 0
scode[2][2][1] = 1
scode[1][2][2] = 2
scode[4][1][1] = 3
scode[1][3][2] = 4
scode[2][3][1] = 5
scode[1][1][4] = 6
scode[3][1][2] = 7
scode[2][1][3] = 8
scode[1][1][2] = 9

def solve():
    res = 0
    # 뒤에서 1을 찾아서 바로 위에 0이 잇는 셀을 찾기
    for i in range(N): # 행
        j = M*4-1
        while j >= 55:
            if arr[i][j] == 1 and arr[i-1][j] == 0: # 1찾고, 바로 위가 0인지 확인
            # 0:1:0:1를 비율 찾기
                code = [0]*8
                for k in range(7,-1,-1):
                    x=y=z=0
                    while arr[i][j] == 1:
                        z += 1
                        j -= 1
                    while arr[i][j] == 0:
                        y += 1
                        j -= 1
                    while arr[i][j] == 1:
                        x += 1
                        j -= 1
                    while arr[i][j] == 0:
                        j -= 1
                    # 1:0:1 의 비율
                    d = min(x,y,z)
                    x //= d
                    y //= d
                    z //= d

                    code[k] = scode[x][y][z]
                odd = code[0]+code[2]+code[4]+code[6]
                even = code[1]+code[3]+code[5]+code[7]
                if (odd * 3 + even)%10 == 0:
                    res += odd + even
                    # 같은 행에 암호코드 블럭이 겹쳐 있다면 다음 암호블럭에 도착
                    # j를 오른쪽으로 한칸 이동해야 함
                j += 1

            j -= 1
    return res

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [[0]*(M*4) for _ in range(N)]

    # 16진수를 2진수로 변환해서 입력받기
    for i in range(N):
        temp = input()
        for j in range(M):
            ch = temp[j]
            if ch <= '9': # 아라비아숫자
                dec = ord(ch) - ord('0') # ord 문자 -> 유니코드 정수
            else: # 알파벳(A~F)
                dec = ord(ch) - ord('A') + 10
            ss = int(ch,16)
            print(dec == ss)
            for k in range(4):
                arr[i][j*4+k] = hex[dec][k]
    print(f'#{tc} {solve()}')
