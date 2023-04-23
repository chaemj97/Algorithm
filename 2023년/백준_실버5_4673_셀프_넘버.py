'''
    접근법 1
        d(n)을 n과 n의 각 자리수를 더하는 함수

'''

def d(n):
    n = n + sum(map(int,str(n)))
    return n

not_self = set()
for i in range(1, 10001):
    not_self.add(d(i))

for j in range(1, 10001):
    # 셀프 넘버인가?
    if j not in not_self:
        print(j)