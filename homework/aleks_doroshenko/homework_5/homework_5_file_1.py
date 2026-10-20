person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)


a = 'результат операции: 42'
b = a.index(':')
c = int(a[b + 2:])
print(c + 10)



a = 'результат операции: 514'
b = a.index(':')
c = int(a[b + 2:])
print(c + 10)

a = 'результат работы программы: 9'
b = a.index(':')
c = int(a[b + 2:])
print(c + 10)


students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
join_students = ', '.join(students)
join_subjects = ', '.join(subjects)
text_exit = 'Students {0} study these subjects: {1}'
print(text_exit.format(join_students, join_subjects))
