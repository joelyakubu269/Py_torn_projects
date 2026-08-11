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
