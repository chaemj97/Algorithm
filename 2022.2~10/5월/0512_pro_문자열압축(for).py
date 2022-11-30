# https://chaemi720.tistory.com/135
def solution(s):
    # 최초에 문자열이 분할이 안되면 결국 입력된 문자열의 길이가 최소의 길이가 됨
    answer = len(s)  

    # 문자열을 앞출할때 최소단위는 1에서 문자열길이의 반이다
    for step in range(1, len(s) // 2 + 1):  
        # 예를 들어 aaa 면 3a abcabc면 2abc 지만 abcdabc는 압축할 수 없다.
        # 압출 결과
        compressed = ''
        # 처음 압출할 문자열 
        prev = s[0:step]
        # 반복 갯수  
        count = 1  
        # step만큼 압축하기로 했으므로 step만큼 건너뛴다.
        for j in range(step, len(s), step):
            # 다음 스텝만큼 갔는데 압축할 문자열이랑 같으면  
            if prev == s[j:j + step]:
                # 반복 갯수 추가  
                count += 1
            # 같지 않다면  
            else:  
                # 압축한 문자열이 2이상부터 숫자를 메길 수 있음
                if count >= 2:  
                    # 압축한 문자열을 카운트한 숫자와 합침
                    compressed += str(count) + prev  
                # 갯수가 1이면 생략
                else:  
                    compressed += prev
                # 이전에 저장된 압축문자열과 다르므로 새로운 압축문자열로 선정
                prev = s[j:j + step]  
                # 다시 1부터 갯수 세기
                count = 1  

        # 맨마지막꺼 고려해주기
        if count >= 2:  
            compressed += str(count) + prev  
        else:  
            compressed += prev

        # 완성된 압축 문자열과 현재 answer로 정의된 것 길이비교해서 작은걸로 선정
        answer = min(answer, len(compressed))  
    return answer