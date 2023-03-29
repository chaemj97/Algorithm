import sys
sys.stdin = open('sample_input.문자열비교.txt')

# T : 테스트 케이스 개수
T = int(input())
for tc in range(1, T + 1):
    # str2 안에 str1과 일치하는 부분이 있으면 1, 아니면 0
    str1 = list(input())
    str2 = list(input())

    # i : str1의 idx, j : str2의 idx
    i = 0
    j = 0

    # str2 안에 str1과 일치하는 부분이 있으면 1, 아니면 0
    result = 0
    # 각 요소 같은지 비교
    # 같으면 둘다 다음 요소 비교
    # str1의 마지막요소까지 다 같으면 1
    # 다르면 str1은 첫번째로 str2는 다음으로
    while j <= len(str2) - 1:
        if str1[i] == str2[j]:
            i += 1
            j += 1
        else:
            i = 0
            j += 1
        if i == len(str1):
            result = 1
            break

    print(f'#{tc} {result}')