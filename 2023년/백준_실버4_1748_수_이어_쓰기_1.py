'''
    접근법
        한 자릿수 1~9, 두 자릿수 10~99, 세 자릿수 100~999
        한 자릿수 총 길이 합 9*1 == 9
        두 자릿수 총 길이 합 90*2 == 180
        세 자릿수 총 길이 합 900*3 == 2700
        i 자릿수 총 길이 합 9*(10**(i-1))*i
        
        ex) n이 4자리 수라면
        9 + 180 + 2700 + (1000에서 n까지 자릿수)
    
'''
import sys
input = sys.stdin.readline

# 1부터 n까지의 수 이어서 쓴 후 자릿수 구하기
n = input().rstrip()

answer = 0
# 1~len(n)-1 자릿수 총 길이 합 구하기
for i in range(1,len(n)):
    answer += 9*(10**(i-1))*i
    
# len(n) 자릿수 총 길이 합 구하기 
answer += (int(n) - 10**(len(n)-1)+1)*len(n)

print(answer)