# dictionary 값만 보기
# list(dict.values())

# 양쪽 공백 제거
# S = S.strip()
# 오른쪽 공백 제거
# S = S.rstrip()
# 왼쪽 공백 제거
# S = S.lstrip()

# 문자열 뒤집기
# 'Hello'[::-1]

# list.sort() : 원본 변경, return None
# sorted(list) : 원본 변경X, return 정렬 결과

# set 요소 삭제
# set.remove(x) : 만약 x가 없다면 keyError
# set.discard(x) : 만약 x가 없으면 pass

for i in range(4):
    for j in range(i+1,5):
        print(i,j)