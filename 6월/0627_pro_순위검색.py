# https://chaemi720.tistory.com/188

# 정확성만 통과
# from itertools import combinations
# import re

# # 지원자의 가능
# def person_case(person,q):
#     for n in range(5):
#         for com in combinations(person,n):
#             k = "".join(com)
#             if k == q:
#                 return True
#     return False
        

# def solution(info, query):
#     answer = []
#     for q in query:
#         q = q.split(' ')
#         score = int(q[-1])
#         q = "".join(q[:-1])
#         # 조건에 and와 - 부분 지우기
#         q = re.sub('and','',q)
#         q = re.sub('-','',q)
#         cnt = 0
#         for person in info:
#             person = person.split(' ')
#             s = int(person[-1])
#             if score <= s:
#                 if person_case(person[:-1],q):
#                     cnt += 1
#         answer += [cnt]
            
#     return answer

# 지원자들 정보, 개발팀이 원하는 조건
def solution(info, query):
    # 나올 수 있는 모든 조건
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())

    # 지원자들이 해당할 수 있는 조건에 점수 넣기
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    # 지원자 점수 오름차순 정렬
    for k in data:
        data[k].sort()

    # 개발자가 원하는 조건에 맞는 인원 수
    answer = list()

    for q in query:
        q = q.split()
        # 개발자가 원하는 조건에 해당하는 사람들의 점수
        scores = data[(q[0], q[2], q[4], q[6])]
        # 개발자가 원하는 점수보다 높은 사람 수 세기 -> 이분 탐색
        wanted = int(q[7])
        l,r = 0, len(scores)
        while l < r:
            middle = (l + r)//2
            if scores[middle] >= wanted:
                r = middle
            else:
                l = middle + 1
        answer.append(len(scores)-l)

    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info,query))