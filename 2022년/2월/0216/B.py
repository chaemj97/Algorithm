# # 연습문제 1
# s = 'Reverse this strings'
#
# N = len(s)
# mid = len(s)//2
# # 리스트로 바꾸어 자리 바꾸기
# s_lst = list(s)
# for i in range(mid):
#     s_lst[i], s_lst[N-1-i] = s_lst[N-1-i], s_lst[i]
#
# print(''.join(s_lst))
#
# # 연습문제 1-1(나)
# def myReverse(strV):
#     N = len(strV)
#     lst = list(strV)
#     result = []
#     for i in range(N):
#         result.append(lst[N-i-1])
#     return result
#
# print(''.join(myReverse(s)))
#
# # 연습문제 1-2(보강)
# def myReverse2(strV):
#     N = len(strV)
#     result = ''
#     for i in range(N-1,-1,-1):
#         result += strV[i]
#     return result
#
# print(myReverse2(s))
# print('==============================')

# 연습문제 2
# chr : 아스키 코드에 해당하는 문자 반환
# ord : 문자의 아스키 코드 반환

# 숫자를 문자로 만들기 123 ->'123'
# 숫자에서 각 자리 별로 숫자 떼어내기
# 떼어낸 숫자를 문자로 변환
# 이전에 떼어서 문자로 변환해 놓은 것에 더하기
def itoa(number):
    # number를 문자열로 만들기
    # 숫자 한 자리씩 떼기 : % 10
    result = ''
    while number:
        # number는 계속해서 나누기 10한 몫만 저장할 것이기 때문에..언젠가는 0이 된다.
        quotient = number // 10
        remain = number % 10
        # 한 자리를  떼어 냈으니... 떼어낸 숫자를 문자로 변환
        # '3'이라는 문자열을 만들고 싶으면, chr(51)
        # 앞쪽 문자가 뒤로 감
        result = chr(remain + ord('0')) + result
        number = quotient
    return result
print([itoa(123)])

# 연습문제 2-1(보강)
a = '342'
b = int(a) # atoi
c = str(b) # itoa

def atoi(strV):
    # '3' => 3 => (0*10)+3
    # '4' => 4 => (3*10)+4
    # '2' => 2 => (34*10)+2
    value = 0
    for c in strV:
        value = value*10 + (ord(c) - ord('0'))
    return value

def itoa(value):
    # 342%10 => 2 => chr(ord('0') + 2) == '2'
    # 34%10 => 4 => '4'
    # 3%10 => 3 => '3'
    strV = ''

    #tmp = value
    isMinus = False
    if value < 0:
        isMinus = True
        value = value*(-1)

    while value > 0:
        r = value%10
        value = value//10
        strV = chr(ord('0')+r) + strV


    #if tmp < 0:
    if isMinus:
        strV = '-' + strV

    return strV
b = atoi(a)
c = itoa(b)
d = itoa(-342)
print(a, type(a), b, type(b), c, type(c), d, type(d))


print('==============================')
