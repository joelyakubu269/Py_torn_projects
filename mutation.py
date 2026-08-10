# this is exercise is to show mutation and reassignment
x= 10
y= x
x= 20
print(x) # prints 20 becuase x has been reassigned, a new x was created
print(y) # it still points to the old x becuase it was not mutated just reassigned
