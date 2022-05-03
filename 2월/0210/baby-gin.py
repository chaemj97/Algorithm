# 완전 탐색으로 babygin을 검사하는 방법은 순열(Permutation)을 만들어보는 것이다.
# 앞쪽과 뒤쪽의 숫자를 각각 세개씩 잘라서 해당 숫자가 run 또는 triplet 인지 검사
# 순열 만들기 - 개수가 정해져 있는 경우 반복문으로 순열 생성 가능
# 각 자리에 들어갈 수 있는 경우의 수 모두 고려해보기 : 완전탐색

def check_baby(arr):
    #첫 번째 자리
    for i in range(6):
        # i 가 첫 번째 자리에 들어갈 요소의 인덱스
        for j in range(6):  # 두 번째 자리에 들어갈 요소 경우의 수 넣어보기
            #j 도 0번째 1번째, 2번째 모든 요소가 될 수 있지만
            #단, i와 같으면 안됨
            if i == j:
                continue
            #겹치지 않는다면,
            for k in range(6):  # k: 세 번째 자리에 들어갈 요소의 인덱스
                # k 역시 앞쪽에서 선택된 요소는 선택할 수 없음
                if k == i or k == j :
                    continue
                #여기서는 i,j,k 가 모두 다름
                for a in range(6): # a: 네 번째 자리에 들어갈 요소의 인덱스
                    if a == i or a==j or a == k :
                        continue
                    for b in range(6):
                        if b == i or b == j or b == k or b == a: # b: 다섯 번째 자리에 들어갈 요소의 인덱스
                            continue
                        for c in range(6): # c: 여섯 번째 자리에 들어갈 요소의 인덱스
                            if c == i or c == j or c == k or c == a or c == b:
                                continue
                            # 순열을 만들어 내는걸 확인했으니.....
                            # 순열 중에 baby-gin이 있는지 확인하기

                            # 앞 3개
                            # run 검사 각각 1차이
                            result = 0  #앞 부분과 뒷부분에서 run 또는 triplet이 몇개 나왔는지 저장하는 변수
                            if arr[i]+1 == arr[j] and arr[i]+2== arr[k]:
                                result += 1
                            # triplet 검사는 다 똑같음
                            elif arr[i] == arr[j] and arr[i] == arr[k]:
                                result += 1

                            # 뒤 3개
                            if arr[a] + 1 == arr[b] and arr[a] + 2 == arr[c]:
                                result += 1
                            elif arr[a] == arr[b] and arr[a] == arr[c]:
                                result += 1

                            if result == 2: # baby-gin
                                #베이비진임을 확인하면.. 다른 경우의 수는 확인 할 필요가 없음!
                                return True
    #반복문 다 수행할 동안 return이 안됐으면, baby-gin이 아님!
    return False

arr = [2, 7, 3, 4, 5, 7]
result = check_baby(arr)
if result:
    print('baby-gin!')
else:
    print('not baby-gin')
# not baby-gin
