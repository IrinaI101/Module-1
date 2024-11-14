immutable_var = 5, 8, 10, True, 'cat'
print(immutable_var)
#immutable_var[2] = 25
#print(immutable_var)
immutable_var_2 = [5, 8, 10], True, 'cat'
print(immutable_var_2)
immutable_var_2[0][2] = 25
print(immutable_var_2)
mutable_list = ['butterfly', 0.25, False, 48]
print(mutable_list)
mutable_list[1] = 'sky'
print(mutable_list)
mutable_list.append(5.25)
print(mutable_list)
mutable_list.extend(['table', 300])
print(mutable_list)
mutable_list.remove('butterfly')
print(mutable_list)
mutable_list.insert(3, 'glass')
print(mutable_list)

