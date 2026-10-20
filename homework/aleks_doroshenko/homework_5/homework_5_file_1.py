person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)


a = 'результат операции: 42'
b=a.index(':')
print(a, b)



students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
join_students = ', '.join(students)
join_subjects = ', '.join(subjects)
text_exit = 'Students {0} study these subjects: {1}'
print(text_exit.format(join_students, join_subjects))
