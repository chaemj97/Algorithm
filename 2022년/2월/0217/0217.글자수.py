import sys
sys.stdin =open('sample_input.글자수.txt')

# T : 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # str1에 포함된 글자들이 str2에 몇개씩 들어있는지
    str1 = input()
    str2 = input()
    # max_result : 그 중 가장 큰 숫자
    max_result = 0
    # 하나하나 비교
    for i in str1:
        result = 0
        for j in str2:
            # 같으면 result 1추가
            if i == j:
                result += 1
        # result가 이전 max_result보다 크면 교체
        if max_result < result:
            max_result = result
    print(f'#{tc} {max_result}')
