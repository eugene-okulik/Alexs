my_dict = {
    'my_tuple': (1, False, 'independent', 45, 5.2, True),
    'my_list': [1, True, 'book', 4.5, 43, 9, 3],
    'another_dict': {'one': 4, 'two': 'pycharm', 'three': False, 'four': 'task', 'five': 5.2},
    'my_set': {2, False, 34, 'simple_text', 6.7, 99, 4, 4}
}
print(my_dict['my_tuple'][-1])
my_dict['my_list'].append(345)
my_dict['my_list'].pop(1)
my_dict['another_dict']['six'] = 'added_element'
my_dict['another_dict'].pop('three')
my_dict['my_set'].add(55.76)
my_dict['my_set'].pop()

