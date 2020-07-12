# def num_of_items_in_list(*args):
#     if len(args) == 0:
#         return args
#     else:
#         return len(args)
#
# print(num_of_items_in_list(3, 8, '9gggb', 'i', 9, 0, 9, 7))


some_data = input('Введите что-то ')


def func_sum_dgt_in_some_data():
    some_data1 = some_data
    import re
    nums = re.findall(r'\d*\.\d+|\d+', some_data1)
    nums = [float(i) for i in nums]
    sum_nums = 0
    for i in nums:
        sum_nums = sum_nums + i
    return sum_nums


# print('Ваша сумма:', func_sum_dgt_in_some_data())


def num_of_unique_param():
    some_data2 = some_data
    b = some_data2.split()
    y = set(b)
    t = list(y)
    r = len(t)
    return r


# print('Уникальных параметров:', num_of_unique_param())


def param_longer_5_chr():
    ml = []
    some_data3 = some_data
    smspl = some_data3.split()
    nl = list(smspl)
    for i in nl:
        if len(i) > 5:
            ml.append(i)
    return ml


# print('Параметры длиннее 5 символов:', param_longer_5_chr())

def my_cool_func():
    print('Ваша сумма:', func_sum_dgt_in_some_data())
    print('Уникальных параметров:', num_of_unique_param())
    print('Параметры длиннее 5 символов:', param_longer_5_chr())


my_cool_func()


