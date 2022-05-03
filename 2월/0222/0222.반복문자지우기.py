# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # 테스트 케이스
    arr = list(map(str,input()))
    # 뒤에서 부터 확인
    # i : 리스트이 마지막 인덱스
    i = len(arr)-1
    while i and len(arr) > 1:
        # 인덱스에러 나지 않도록
        if 0 < i < len(arr):
            # 같으면 삭제
            # arr[i-1]을 삭제하면 i-1뒤의 인덱스들이 1개씩 작아짐
            if arr[i-1] == arr[i]:
                arr.pop(i-1)
                arr.pop(i-1)
        # 다음 비교
        i -= 1
    result = len(arr)

    print(f'#{tc} {result}')

#교수님
# 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # 테스트 케이스
    arr = input()
    stack = []
    # data 하나씩 읽으면서 push
        # 만약에 top에 있는 요소가 나랑 같으면,pop 아니면 push
    for i in arr:
        # 비어있으면 무조건 넣기
        if not stack:
            stack.append(i)
        else:
            # top이 나랑 같은가
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
    print(f'#{tc} {len(stack)}')