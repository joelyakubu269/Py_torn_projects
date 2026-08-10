# this is exercise is to show mutation and reassignment
x= 10
y= x
x= 20
print(x) # prints 20 becuase x has been reassigned, a new x was created
print(y) # it still points to the old x becuase it was not mutated just reassigned
a= [10,20,30]
b= a
a.append(40)
print(a) # the both print the same result because append changes the original value
print(b) # the both point to the same value and append changes that value so they both change
