import decimal as de
array = [1,2,3,4,5]
print(all(array))

number_array = [1,2,3,4,5]


de.getcontext().prec = len(number_array)

for i in range(1,11):
    number_array.append(i)


array = range(1,11)
print(array)


