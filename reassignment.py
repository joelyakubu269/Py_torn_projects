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
