v1 = input('Введите значение ')
try:
    v2 = float(v1)
    print('Значение - число с пл.зап', type(v2))
    if (v2 > 9) and (v2 < 20):
        print('Число в диапазоне от 10 до 20')
    elif (v2 > 19) and (v2 < 30):
        print('Число в диапазоне от 20 до 30')
    elif v2 < 0:
        print('Число меньше 0, преобразовано в положительное', abs(v2))
    else:
        print('Другое значение числа')
    try:
        v3 = int(v1)
        print('Значение целочисленное', type(v3))
        v4 = v3 ** 3 if (v3 > 0) else v3 ** 2
        print(v4)
    except:
        pass
    finally:
        pass
except ValueError:
    v4 = str(v1)
    print('Значение строка', type(v4))
    if v4 == '':
        print('Строка пустая')
    if v4 != '' and 'abc' in v4:
        print('Последовательность abc найдена')
    if v4 != '' and 'abc' not in v4:
        print('Последовательность abc НЕ найдена')
finally:
    try:
        if v2 != '' and v3 != '':
            print('Результат:')
            print('с пл.зап, целочисленное - ок')
    except:
        if v4 != '':
            print('Результат:')
            print('строковое ок')
    finally:
        pass