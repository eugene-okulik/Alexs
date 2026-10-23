a = 'результат операции: 42'
b = 'результат операции: 54'
c = 'результат работы программы: 209'
d = 'результат: 2'


def sum_number(number):
    print(int(number.split()[-1]) + 10)


for number in (a, b, c, d):
    sum_number(number)
