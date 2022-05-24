def solution(new_id):
    answer = ''
    # 1. 모두 소문자
    new_id = new_id.lower()
    # 2. 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)만 허용
    no = new_id.maketrans('~!@#$%^&*()=+[{]}:?,<>/','                       ')
    new_id = new_id.translate(no).replace(' ','')
    # 3. 마침표(.)가 2번 이상 연속된 부분 하나의 마침표로 치환
    i = 0
    while i < len(new_id)-1:
        if new_id[i] == '.' and new_id[i+1] == '.':
            new_id = new_id[0:i+1]+new_id[i+2:]
        else:
            i += 1
    # 4. 처음이나 끝에 마침표(.) 있다면 제거
    new_id = new_id.strip('.')
    # 5. 빈 문자열이면, 'a'
    if new_id == '':
        new_id = 'a'
    # 6. 길이가 16 이상이면, 첫 15개 문자만 쓰기, 맨 뒤 마침표인지 확인
    if len(new_id) >= 16:
        new_id = new_id[0:15].strip('.')
    # 7. 길이가 2 이하, 길이가 3이 될 때까지 마지막 문자 추가를 반복
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    answer = new_id
    return answer
print(solution("......a......a......a....."))