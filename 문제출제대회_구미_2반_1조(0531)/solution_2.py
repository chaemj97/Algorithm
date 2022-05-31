import sys
sys.stdin = open('testcase.txt')

block = [4, 3, 2, 1]

tc = int(input())
for test in range(1, tc+1):
    N, M = map(int, input().split())
    myMap = list(map(int, input().split()))
    min_v = min(myMap)
    res = []
    for i in myMap:
        res.append(i - min_v)

    result = 0
    for _ in range(200):
        min_v = min(res)
        idx_list = []
        for i, v in enumerate(res):
            if v == min_v:
                idx_list.append(i)
        if len(idx_list) == len(myMap):
            break
        for idx in idx_list:
            if res[idx] == min_v:
                for d in block:
                    if 0 <= idx + d <= len(myMap):
                        for i in res[idx:idx+d]:
                            if i != res[idx]:
                                break
                        else:
                            for i in range(idx, idx+d):
                                res[i] += 1
                            else:
                                result += 1
                                break
        min_v = min(res)
        for i, v in enumerate(res):
            res[i] -= min_v
    if result <= M:
        print(f'#{test} {result}')
    else:
        print(f'#{test} FAIL')
