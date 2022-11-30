# https://chaemi720.tistory.com/158

# 설탕 3킬로그램 봉지, 5킬로그램 봉지
# 배달 N킬로그램
N = int(input())

result = 0
while N > 0:
    # 5의 배수면 설탕 봉지 수 계산 끝
    if N%5 == 0:
        result += N/5
        break
    # 5의 배수 아니면 3킬로그램 설탕
    else:
        N -= 3
        result += 1
        # 만약 음수면 실패
        if N < 0:
            result = -1

print(int(result))