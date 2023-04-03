'''
    접근법 1
        리스트로 검색시 시간초과 날 수 있으니
        dict의 key: value를 활용

'''

import sys
input = sys.stdin.readline

# 포켓몬의 개수, 내가 맞춰야 하는 문제의 개수
N,M = map(int,input().split())
# 포켓몬
# {id:name}
poketmon = {i:input().rstrip() for i in range(1,N+1)}
# {name:id}
poketmon_id = {v:k for k,v in poketmon.items()}
# 찾기
for _ in range(M):
    search = input().strip()
    # 숫자면 포켓몬 이름
    if search.isdigit():
        print(poketmon[int(search)])
    # 문자면 포켄몬 번호
    else:
        print(poketmon_id[search])

