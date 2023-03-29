# https://chaemi720.tistory.com/154

# from itertools import combinations

# # 암호의 길이 L, 암호로 사용했을 법함 문자의 종류 C
# L, C = map(int,input().split())
# word = list(input().split())

# # 암호 문자 증가하는 순서로 배열
# # 문자도 .sort()하면 오름차순으로 정렬!!
# word.sort()

# # L개씩 조합으로 뽑기
# for i in combinations(word,L):
#     # 모음의 개수 세기
#     cnt = 0
#     cnt += i.count('a')
#     cnt += i.count('e')
#     cnt += i.count('i')
#     cnt += i.count('o')
#     cnt += i.count('u')
#     # 모음 1개 이상, 자음 2개 이상(모음의 개수가 최대 L-2)이면 출력
#     if 1 <= cnt <= L-2:
#         print(''.join(i))

# -----------------------------------------
from itertools import combinations
# 암호의 길이 L, 암호로 사용했을 법함 문자의 종류 C
L, C = map(int,input().split())
word = list(input().split())

# 암호 문자 증가하는 순서로 배열
# 문자도 .sort()하면 오름차순으로 정렬!!
word.sort()

# 모음
vowel = set('aeiou')
for i in combinations(word,L):
    # 차집합을 통해 자음 구하기
    consonant = set(i)-vowel
    # 자음 2개 이상, 모음 1개 이상(자음 최대 L-1)인가?
    if 2 <= len(consonant) <= L-1:
        print(''.join(i))

