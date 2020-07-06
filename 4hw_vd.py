var_f = 'Whose 45 footprints 67 finished 89 by the fence 00'
print('Replace the first two occurrences F: ', var_f.replace('f', 'F', 2))
var_f_count = var_f.count(' ')
print('Number of spaces per line: ', var_f_count)
var_f_count_to_str = str(var_f_count)
var_f2 = var_f + var_f_count_to_str
print('Add number in spaces to end of line: ', var_f2)
print('ok endswith') if var_f2.endswith(var_f_count_to_str) else print('not endswith ok')
var_f3 = var_f2.upper()
print(var_f3)
print('ok upper') if var_f3.isupper() else print('not upper ok')
var_f4 = var_f3[3::4]
print('Every fourth:', var_f4)
del_digit = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
var_f5 = var_f4
var_f5 = ''.join(i for i in var_f5 if not i in del_digit)
print('Delete all digits from a string: ', var_f5)


import re  # тут , наверное, я не так поняла задание?
var = 'При помощи регулярок реализовать АА1256ББ поиск автомобильного номера АА1234ББ'
var1 = print(re.findall('\АА1234ББ\w{0}', var))