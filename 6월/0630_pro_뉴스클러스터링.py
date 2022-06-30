# https://chaemi720.tistory.com/193

def solution(str1, str2):
    
    # 모두 대문자로 바꾸기
    str1 = str1.upper()
    str2 = str2.upper()
    
    # 다중 집합 만들기
    # 영어로만 되어있는게 아니면 버리기
    one = []
    two = []
    for i in range(0,len(str1)-1):
        s = str1[i:i+2]
        if s.isalpha():
            one.append(s)
    for j in range(0,len(str2)-1):
        s = str2[j:j+2]
        if s.isalpha():
            two.append(s)

    # 둘 다 공집합이면
    if len(one) == len(two) == 0:
        return 65536
    # 한 쪽이 공집합
    elif len(one) == 0 or len(two) == 0: 
        return 0
    
    one.sort()
    two.sort()
    
    # 교집합
    intersection = []
    
    for a in range(len(one)):
        for b in range(len(two)):
            if one[a] == two[b]:
                intersection.append(one[a])
                two.pop(b)
                break
    
    # 합집합
    union_length = len(intersection) + (len(one) - len(intersection)) + (len(two))
    
    
    # 교집합 수/합집합 수
    answer = len(intersection)/union_length
    return int(answer * 65536)