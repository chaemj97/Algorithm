# https://chaemi720.tistory.com/165

from sys import stdin

# # 단어의 개수
# N = int(input())
# # 같은 단어 제외하기 위해 set
# words = [set() for _ in range(51)]
# # 길이가 같은 문자끼리 함께 넣기
# for _ in range(N):
#     word = stdin.readline().rstrip()
#     words[len(word)].add(word)
#
# # 길이가 적은 순으로 사전식 정렬해서 출력
# for i in range(1,51):
#     if words[i]:
#         i_list = sorted(list(words[i]))
#         for j in i_list:
#             print(j)

# 단어의 개수
N = int(input())
# 단어를 중복 제거 후 리스트로
words = list(set(stdin.readline().rstrip() for _ in range(N)))
# 단어를 길이순정렬 + 사전식정렬
words.sort(key=lambda x :(len(x),x))
for word in words:
    print(word)