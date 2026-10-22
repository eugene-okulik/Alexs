a = 'результат операции: 42'
b = 'результат операции: 54'
c = 'результат работы программы: 209'
d = 'результат: 2'

def sum_number(num):
    print(int(num.split()[-1]) + 10)

for num in (a, b, c, d):
    sum_number(num)

