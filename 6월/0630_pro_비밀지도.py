# https://chaemi720.tistory.com/194

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        # 2진수로 바꾸기 / n자리 0으로 채우기
        a = bin(arr1[i])[2:].zfill(n)
        b = bin(arr2[i])[2:].zfill(n)
        result = ''
        # 둘다 0이면 빈칸 / 아니면 벽
        for j in range(n):
            if a[j] == b[j] == '0':
                result += ' '
            else:
                result += '#'
        answer.append(result)
    return answer