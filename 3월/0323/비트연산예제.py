# 예제 1
'''
def Bbit_print(i):
    output = ""
    for j in range(7,-1,-1):
        output += '1' if i & (1<<j) else '0'
    print(output)
for i in range(-5,6):
    print('%3d = ' % i, end='')
    Bbit_print(i)
'''

# 예제 2
'''
# 16진수 1자리 = 2진수 4자리
def Bbit_print(i):
    output = ""
    for j in range(7,-1,-1):
        output += '1' if i & (1<<j) else '0'
    print(output,end=' ')
a = 0x10 # 16진수
x = 0x01020304
print('%d = ' % a,end=' ')
Bbit_print(a)
print()
print('0%X = ' % x, end=' ')
for i in range(0,4):
    # oxff : 255 : 11111111(2)
    Bbit_print((x>>i*8) & 0xff)
'''

# 예제 3
