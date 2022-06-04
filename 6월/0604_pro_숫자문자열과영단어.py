def solution(s):
    answer = ''
    # 영어 : 숫자
    en = {'zero':'0','one':'1','two':'2','three':'3','four':'4',
          'five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    english = ''
    for i in s:
        # 숫자면 바로 넣기
        if i in '0123456789':
            answer += i
        # 영어면 영단어 완성할 때까지
        else:
            english += i
        # 영단어가 완성되면 넣기
        try:
            answer += en[english]
            english = ''
        except:
            pass
    return int(answer)


def solution2(s):
    # 영어 : 숫자
    en = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
          'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    answer = s
    # 영단어를 바로 숫자로 바꾸기
    for key, value in en.items():
        answer = answer.replace(key, value)
    return int(answer)