# 그룹 나누기
def grouping(start, end):
    # 그룹에 1명이 되는경우
    # 예를들어 3명을 grouping하면 1명 / 2명 으로 나누어짐
    if start == end:
        return start

    first_v = grouping(start,(start+end)//2)
    second_v = grouping((start+end)//2+1,end)
    return rcp(first_v,second_v)

# 가위바위보 결과
# 1은 가위, 2는 바위, 3은 보 : 1<2, 2<3, 3<1 -> 차이가 1일 때 숫자 큰거, 차이가 2일 때 숫자 작은거 이김
# 같으면 번호 작은 쪽이 이김
def rcp(a,b):
    if arr[a] == arr[b]:
        return a
    elif abs(arr[a]-arr[b]) == 1:
        if arr[a] > arr[b]:
            return a
        else:
            return b
    elif abs(arr[a]-arr[b]) == 2:
        return a if arr[a] < arr[b] else b


# 테스트 케이스
T = int(input())
for tc in range(1,T+1):
    # 인원수
    N = int(input())
    # N명이 고른 카드 번호순
    arr = list((map(int,input().split())))
    start = 0
    end = N-1
    print(f'#{tc} {grouping(start,end)+1}')

