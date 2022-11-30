
# 사람 수, 파티 수
N, M = map(int,input().split())
# 진실을 아는 사람 수, 번호
true_p = list(map(int,input().split()))[1:]

# 진실 아는 사람 1, 모르면 0
know = [0]*N
for i in true_p:
    know[i-1] = 1

# 파티
party = [list(map(int,input().split()))[1:] for _ in range(M)]
# 진실을 말해야 하는 파티면 1, 아니면 0
true_party = [0]*M

#
while true_p:
    know_person = true_p.pop()

    # know_person이랑 같은 파티에 있는 사람들은 이제 진실을 들었다.
    for i in range(M):
        if know_person in party[i]:
            # 이제 이 파티는 진실만 말해야해
            true_party[i] = 1
            for j in party[i]:
                # 이 사람이 진실을 이번에 알았다면 true_p에 추가/know[j] 1로 바꾸기
                if know[j-1] == 0:
                    true_p.append(j)
                    know[j-1] = 1

# 거짓말해도 되는 파티
print(true_party.count(0))