immutable_var = 1, 2, 'Привет'
print(immutable_var)
#immutable_var[0] = 30
# Изменить индекс [0] нельзя, потому что данные в кортеже не изменяемы, кортеж это грубо говоря хранилеще, то что мы хотим оставть не изменным

mutable_list = [1, 2, 'fire']
print(mutable_list)
mutable_list [1] = 40
print(mutable_list)
mutable_list [0] = 39
print(mutable_list)
mutable_list.remove('fire')
print(mutable_list)