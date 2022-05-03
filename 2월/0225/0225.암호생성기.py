# 테스트 케이스의 개수 : 10
for _ in range(1,11):
    # 테스트 케이스 번호
    TC = int(input())
    data = list(map(int,input().split()))

    while data[-1] > 0:
        for j in range(1,6):
            # 맨 앞 수에 j 만큼 빼주고(뺐을 때 그 수가 0보다 작으면 멈추기) 맨뒤로 보내기
            # 맨 앞 자리는 삭제
            new = data[0] - j
            if data[0]-j <= 0:
                new = 0
                data.append(new)
                data.pop(0)
                break
            else:
                data.append(new)
                data.pop(0)

    print(f'#{TC}', *data)