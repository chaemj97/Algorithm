# 0000000111100000011000000111100110000110000111100111100111111001100111
# 7개 비트씩 읽어와서 10진수로 변환
binary = list(map(int,input()))

for i in range(0,len(binary),7):
    # 7비트를 읽어오는 반복문 작성
    cnt = 6
    sum_v = 0
    for j in range(i,i+7):
        sum_v += binary[j] * 2**cnt
        cnt -= 1
    print(sum_v,end=' ')