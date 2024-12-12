#1.Функция с параметрами по умолчанию
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

#2.Распаковка параметров
values_list = [False, 9, 'Привет']
values_dict = {'result' : False, 'numb' : 9, 'word' : 'Привет'}

print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)