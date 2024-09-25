immutable_var = 3, 5, 7, 'Hello', True
print(immutable_var, ['Комментарий: кортеж в () неизменяемый'])
#immutable_var [0] = 6
#print(immutable_var)
mutable_list = [3, 5, 7, 'Hello', True]
print(mutable_list)
mutable_list[0] =  100
print(mutable_list)
mutable_list[-1] = 'Goodbye'
print(mutable_list)
