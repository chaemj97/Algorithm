# 고지식한 알고리즘
# p : 찾을 패턴, t : 전체 텍스트
def Brute_Force(p,t):
    # 찾을 패턴의 길이
    M = len(p)
    # 전체 텍스트의 길이
    N = len(t)
    # p의 idx
    i = 0
    # t의 idx
    j = 0

    while i < M and j < N:
        # 같지 않다면 t는 시작점을 한 칸 뒤로, p는 맨앞으로,
        # 같으면 다음꺼 비교
        # (둘다 한 칸씩 이동해야하므로 코드 위치 주의!!!)
        if p[i] != t[j]:
            j -= i
            i = -1
        i += 1
        j += 1
    # 검색 성공 : p의 마지막 idx까지 확인
    if i == M:
        return j-M
    # 검색 실패
    else:
        return -1

# 찾을 패턴
p = 'is'
# 전체 텍스트
t = 'Python is funny!'

print(Brute_Force(p,t))
