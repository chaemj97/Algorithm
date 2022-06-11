import re
    

while True:
    s = input()
    # 종료조건(맨 마지막에 점 하나)
    if s == '.':
        break
    # 검사!!
    else:
        # 숫자 영어 점 공백 제거
        s = re.sub('[0-9a-zA-Z. ]','',s)
        # 괄호가 없는거면 통과!
        if s == '':
            print('yes')

  
            
                                
