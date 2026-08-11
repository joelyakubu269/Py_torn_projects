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
print(other2)
