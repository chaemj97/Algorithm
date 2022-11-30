def solution(dartResult):
    answer = 0
    # 점수/보너스/옵션
    dartNum = [['','',''] for _ in range(3)]
    idx = 0
    for i in dartResult:
        # 숫자면 점수 칸에
        if i.isdigit():
            # 연속 숫자가 아니라 다음 다트점수면 idx +1
            if dartNum[idx][1]:
                idx += 1
            dartNum[idx][0] += str(i)
        # SDT 중 하나면 보너스 칸에
        elif i in 'SDT':
            dartNum[idx][1] = i
        # *# 중 하나면 옵션 칸에
        else:
            dartNum[idx][2] = i
    
    # 점수 계산
    for num in range(3):
        # D : 해당 점수 제곱 
        if dartNum[num][1] == 'D':
            dartNum[num][0] = int(dartNum[num][0])**2
        # T : 해당 점수 세제곱
        elif dartNum[num][1] == 'T':
            dartNum[num][0] = int(dartNum[num][0])**3
        
        # 스타상 : 해당 점수와 직전 점수 2배
        if dartNum[num][2] == '*':
            # 해당 점수 2배
            dartNum[num][0] = int(dartNum[num][0])*2
            # 직전 점수가 있다면 그것도 2배
            if num != 0:
                dartNum[num-1][0] = int(dartNum[num-1][0])*2
        # 아차상 : 해당 점수 마이너스
        elif dartNum[num][2] == '#':
            dartNum[num][0] = -int(dartNum[num][0])
            
    # 점수 합
    for c in range(3):
        answer += int(dartNum[c][0])
    return answer