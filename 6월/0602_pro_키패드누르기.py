# https://chaemi720.tistory.com/142

def solution(numbers, hand):
    answer = ''

    # 각 자리
    keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2),
              4: (1, 0), 5: (1, 1), 6: (1, 2),
              7: (2, 0), 8: (2, 1), 9: (2, 2),
              '*': (3, 0), 0: (3, 1), '#': (3, 2)}

    # 현재 엄지의 위치 [왼손, 오른손]
    hands = ['*', '#']

    # 번호 누르기
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            hands[0] = num
        elif num in [3, 6, 9]:
            answer += 'R'
            hands[1] = num

        # 2580
        else:
            # 손가락과 누르고 싶은 키패드 거리 구하기
            want = keypad[num]
            l = keypad[hands[0]]
            r = keypad[hands[1]]
            l_dist = abs(want[0] - l[0]) + abs(want[1] - l[1])
            r_dist = abs(want[0] - r[0]) + abs(want[1] - r[1])

            if r_dist > l_dist:
                answer += 'L'
                hands[0] = num
            elif r_dist < l_dist:
                answer += 'R'
                hands[1] = num
            # 거리가 같으면 어느손잡이인지에 따라
            else:
                if hand == 'left':
                    answer += 'L'
                    hands[0] = num
                else:
                    answer += 'R'
                    hands[1] = num

    return answer