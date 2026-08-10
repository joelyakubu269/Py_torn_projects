x = [10]
y = x

x = [20]
print(x) # prints 20 because its been reassigned
print(y) # prints 10 becuase the original value has not been changed
# aliasing
a= [10,20,30]
b= a
a.append(40)
a[0]= 5
a.remove(20)
print(a) # the both print the same value bcoz they still point to the same value
print(b)
# coppy
numbers = [10,20,30]
copy_numbers = numbers.copy()
copy_numbers.append(40)
print(numbers)
print(copy_numbers) # different result becuase what you do the copy does not affect the original
# deep copy
number = [[10, 20], [30, 40]]
copy_number = number.copy()
number[0][0]= 1
print(number)
print(copy_number)
