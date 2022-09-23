import sys
input = sys.stdin.readline

# 폭발 전 문자열
s = input().strip()
# 폭발 문자
explosion = list(input().strip())
e_len = len(explosion)

# 결과
result = []

# 한개씩 result에 넣기
# 넣었을때 폭발문자가 완성된다? -> pop
for i in s:
    result.append(i)
    if len(result) >= e_len and result[-e_len:] == explosion:
        # result = result[:-e_len]
        for _ in range(e_len):
            result.pop()

# 폭발이 끝난 후 남아있는 문자가 있는가?
if result:
    print(''.join(result))
else:
    print('FRULA')

