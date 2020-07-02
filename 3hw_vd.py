while True:  # task 1, version 1
    try:
        v4 = abs(int(input('Введите целочисленное число ')))
        v5 = 0
        while v4 > 0:
            v4 //= 10
            v5 += 1
        print(v5)
    except:
        print('Ошибка, вы ввели не целочисленное число!')
        continue
    break


while True:  # task 1, version 2
    try:
        v2 = abs(int(input('Введите целочисленное число, версия 2 ')))
        v3 = print(len(str(v2)))
    except:
        print('Ошибка, вы ввели не целочисленное число!')
        continue
    break
