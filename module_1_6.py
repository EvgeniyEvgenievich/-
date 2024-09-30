my_dict = {'Lev':2022, 'Dmitriy':2013, 'July':1993, 'Andrey':1996}
print(my_dict)
print(my_dict.get('Lev'))
print(my_dict.get('evgeniy'))
my_dict.update({'Oleg':1996, 'Denis':2000})
del my_dict['Andrey']
print(my_dict)
my_set = {'Andrey', 2025, False, 2022, False, 2022, 2025, 'Andrey',}
print(my_set)
my_set.add('Lev')
my_set.add(True)
my_set.remove(False)
print(my_set)