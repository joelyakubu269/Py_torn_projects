x = (1, 2, 3)
print(x[0]) # indexing test
print(x[0:2]) #slicing without step
print(x[0::2]) # slicing with step
# you cannot add to a tuple x.append(9)
#tuples are immutable but that does not mean they cannot change
y= (1,2,3)
#y[0].append(9) will give an error
# tuples can be reassigned
y= (4,5,6) # so you see tuples can change but not be modified
# A single tuple with no commas is just an int
a=(8)
b=(8,)
print(type(a))
print(type(b)) # run it and see the difference
# unpacking in tuples ,its also done in lists
x=(1,2,3)
a,b,c = x
print(a)
print(b)
print(c) # it just like give each value a unique variable name
# so why use a tuple when its just a limited version of a list
# its used in instances where you want data constant, like coordinates coordinates = (10.5, 20.3)
# They are also used as Dictionary keys
locations = {
    (0, 0): "Origin",
    (10, 20): "Point A"
}
print(locations)
# lists nested in tuples, what do you think will happen here
c = ([10, 20], [30, 40])

d = c

d[0].append(99)

print(c)
print(d) # tuples are immutable but the list in them are mutable and since c and d point to the same list change in d affects c
