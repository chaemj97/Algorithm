def kmp(t,p):
    # 패턴이 있는지 찾고자 하는 대상문자열 길이
    N = len(t)
    # 패턴의 길이
    M = len(p)

    # lps : Longest proper prefix which is also suffix
    # prefix : 접두사, suffix : 접미사, proper : 적절한
    lps = [0] * (M+1)
    #preprocessing : 전처리
    lps[0] = -1
    # 사전작업 : 매칭이 실패했을 때 패턴의 어느 인덱스로 돌아가야 하는지 계산
    # 일치한 개수를 저장하는 변수
    j = 0
    for i in range(1,M):
        # 어느 위치로 돌아가야 하는지 계산 : 앞쪽에 얼마나 많은 패턴이 맞았는가?
        # p[i] 이전에 일치한 개수
        lps[i] = j
        # 앞서서 패턴이 일치 했으면....j 증가
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j

    print(lps)
    # ===============================

    # 패턴매칭 시작
    # Search
    # 비교할 텍스트 위치
    i = 0
    # 비교할 패턴 시작위치
    j = 0
    while i < N and j <= M:
        # 첫 글자가 불일치 했거나 or 일치하면
        if j == -1 or t[i] == p[j]:
            i += 1
            j += 1
        # 불일치
        else:
            # shift 찾기
            j = lps[j]
        # 패턴을 찾을 경우
        if j == M:
            # 패턴의 인덱스 출력
            return i-M
    return -1

# 예제1
t1 = 'zzzabcdabcdabcdf'
p1 = 'abcdabcdf'
# arr = [0,a,b,c,d,a,b,c,d,f]
# [-1,0,0,0,0,1,2,3,4,0]
# arr[5]의 a는 arr[1]의 a와 같으므로 인덱스 1로 이동
# t의 idx가 7일때 패턴 나타남
print(kmp(t1,p1))
# [-1, 0, 0, 0, 0, 1, 2, 3, 4, 0]
# 7

# 예제2
t2 = 'abcde'
p2 = 'cdd'
print(kmp(t2,p2))
# 패턴 나타나지 않음
# [-1, 0, 0, 0]
# -1