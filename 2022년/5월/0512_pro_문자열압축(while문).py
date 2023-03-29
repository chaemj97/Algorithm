# https://chaemi720.tistory.com/135
def solution(s):
    # 최초에 문자열이 분할이 안되면 결국 입력된 문자열의 길이가 최소의 길이가 됨
    answer = len(s)
    
    # i : 나눌 갯수 1~(문자 길이의 절반)
    for i in range(1,len(s)//2+1):
        # 미리 i개로 나누어 리스트로 정렬
        split_s = []
        for j in range(0,len(s),i):
            split_s += [s[j:j+i]]
        # 압축 결과
        result = ''
        # 반복 갯수
        num = 1
        # 비교 인덱스 start : 기준값, end : 비교값
        start = 0
        end = 1

        while start != len(split_s):
            # end가 index를 벗어났다는 것은 마지막인덱스까지 비교 끝났다는 뜻
            if end == len(split_s):
                # 1은 의미 없으니 추가X
                if str(num) != '1':
                    result += str(num)
                result += split_s[start]
                break
            # 비교해서 같지않다면 압축결과에 반복 갯수와 문자추가
            if split_s[start] != split_s[end]:
                # 단 반복 갯수가 1이면 숫자 추가X
                if str(num) != '1':
                    result += str(num)
                result += split_s[start]
                # 기본값을 비교값으로 옮기기
                # 반복 갯수 1로 초기화
                start = end
                num = 1
            # 비교해서 같다면 반복 갯수 1추가
            else:
                num += 1
            end += 1

        # 압축 길이 비교
        answer = min(answer,len(result))

    return answer
