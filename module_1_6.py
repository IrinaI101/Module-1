my_dict = {'Ivan' : 1995, 'Kate' : 1999, 'Jane' : 2000, 'Victor' : 1996}
print(my_dict)
print(my_dict.get('Victor'))
print(my_dict.get('Mary'))
my_dict.update({'Sophie' : 2001, 'Jack' : 2003})
print(my_dict.pop('Kate'))
print(my_dict)
my_set = {2, 2, 5, 5, 'day', 'day', (1,2,3), (1,2,3)}
print(my_set)
my_set.update(['night', 6])
my_set.discard('day')
print(my_set)


