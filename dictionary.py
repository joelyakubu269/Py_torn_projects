# in this exercise i study the behaviour of dictionaries when i assign, copy,nest and mutate
person = {
    "name": "Joel",
    "age": 25
}

other = person

other["age"] = 30

print(person)
print(other) # print the same value becuase the point to the same value
person1 = {
    "name": "Joel",
    "age": 25
}

other1 = person.copy()

other1["age"] = 30

print(person1)
print(other1) # the reuslts are different because they dont point to the same value while other1 is just a copy
person2 = {
    "name": "Joel",
    "details": {
        "age": 25,
        "country": "Nigeria"
    }
}

other2 = person2.copy()

other2["details"]["age"] = 30

print(person2)
print(other2) # here modifying the copy changes the original because they both have an inner shared dictionary
# Mutating vs Replacing
person3 = {
    "name": "Joel",
    "scores": [70, 80, 90]
}

other3 = person3.copy()

other3["scores"].append(100)

print(person3)
print(other3) # they both print the same thing becuase the dictionaries are seperate entities but share(point to) the same inner list
# Reassigning in Dictionary
person4 = {
    "name": "Joel",
    "scores": [70, 80, 90]
}

other4 = person4.copy()

other4["scores"] = [70, 80, 90, 100]

print(person4)
print(other4) # the dont print the same result because reassigning creates a new list it does not change the original list
# keys in dictionary
# keys can be changed in dictionaries but you have to pop the former key
john = {
    "height": "6ft",
    "age": 24
}
print(john)
john["years"] = john.pop("age") # start with the new key in mind then pop
print(john)
#d = {
#    [1, 2]: "list"
#}
# print(d) this gives an error because a list cannot be used as a key because a list can be changed
# did some exercises to understand dictionary methods
student = {
    "name": "Joe",
    "age": 25,
    "course": "Python"
}
# changing the values
student["name"]= "doe"
student["age"] = 24
print(student)
# Adding a key and value pair
student["level"]= "beginner"
student.pop("course")
print(student)
# to check if a key exsists # could also do if "age" in student print("exists)
print( "age" in student)
for i in (student.keys()):
    print(i)
for j in (student.values()):
    print(j)
for k,v in (student.items()): # print key and value pairs
    print(k,v)
# Another way of getting values
value = student.get("age",None) # we use this None beside bcoz at times the value may be None
if "age" in student:
    print(value)
students = {
    "Joel": {
        "age": 25,
        "scores": [70, 80, 90]
    },
    "David": {
        "age": 23,
        "scores": [60, 75, 80]
    }
}
print(students["Joel"]["age"])
students["Joel"]["scores"].append(100)
print(students)
def mean(students,name):
    counter= len(students[name]["scores"])
    avg= 0
    for i in range(counter):
        total= 0
        total+= students[name]["scores"][i]
        avg= total/counter
    return avg
print(mean(students,"Joel"))
