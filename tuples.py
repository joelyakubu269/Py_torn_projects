x = (1, 2, 3)
print(x[0]) # indexing test
print(x[0:2]) #slicing without step
print(x[0::2]) # slicing with step
# you cannot add to a tuple x.append(9)
#tuples are immutable but that does not mean they cannot change
y= (1,2,3)
#y[0].append(9) will give an error
# tuples can be reassigned
y= (4,5,6)
