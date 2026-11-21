from func import *

l = input('Введите номер уровня: ')
if l == '1':
    level1()
elif l == '2':
    level2()
elif l == '3':
    level3()
elif l == '4':
    level4()
elif l == '5':
    level5()
else:
    print('Данного уровня не существует')
