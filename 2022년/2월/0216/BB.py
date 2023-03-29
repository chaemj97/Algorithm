# 숫자를 문자로 바꾸기
# 123 -> '123'
def itoa(s):
    # 123%10 = > 3 => chr(ord('0')+3) == '3'

    # 음수일 경우 값을 양수로 바꾼 후 계산
    isMinus = False
    if s < 0:
        isMinus = True
        s = -s

    result = ''
    while s:
        value = s%10
        # 더하면 뒤에 붙으므로
        result = chr(value+ord('0')) + result
        s //= 10

    # 음수는 다시 앞에 - 붙이기
    if isMinus:
        result = '-' + result
    return result

# 양수
s1 = 123
print(s1,type(s1))
# 123 <class 'int'>

chr_s1 = itoa(s1)
print(chr_s1,type(chr_s1))
# 123 <class 'str'>

# 음수
s2 = -123
print(s2,type(s2))
# -123 <class 'int'>

chr_s2 = itoa(s2)
print(chr_s2,type(chr_s2))
# -123 <class 'str'>