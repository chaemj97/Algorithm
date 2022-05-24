def solution(new_id):
    answer = ''
    # 1. 모두 소문자
    new_id = new_id.lower()
    # 2. 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)만 허용
    for no in '-_.~!@#$%^&*()=+[{]}:?,<>/':
        new_id.replace(no,'')
    
    return answer