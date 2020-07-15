var_list = ['Whose', '45', 'foo', '67', 'finished', '89', 'by', 'the', 'fence', '00']
var_upper = list(map(lambda x: x.upper(), var_list))
print(var_upper)


def my_bread_decorator(func_to_decorate):
    def wrapper(*args):
        print('Хлеб')
        func_to_decorate(args[0])
        func_to_decorate(args[1])
        func_to_decorate(args[2])
    return wrapper


@my_bread_decorator
def func_bread(*args):
    print(*args)


func_bread('Масло', 'Сыр', 'Помидорка')

