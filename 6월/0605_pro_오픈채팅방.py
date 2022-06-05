# https://chaemi720.tistory.com/147

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
def solution(record):
    answer = []
    user = {}

    # 이름 변경한 사람 처리
    for r in record:
        if r.split()[0] != 'Leave':
            user[r.split()[1]] = r.split()[2]
    
    # 결과 출력
    for r in record:
        if r.split()[0] == 'Enter':
            answer += [f'{user[r.split()[1]]}님이 들어갔습니다.']
        elif r.split()[0] == 'Leave':
            answer += [f'{user[r.split()[1]]}님이 나갔났습니다.']

    return answer

print(solution(record))