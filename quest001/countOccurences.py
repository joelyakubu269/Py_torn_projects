"""
def count_occur(numbers, target): # this code gives us the amount of times a target nuumber appears
    count=0
    for c in numbers:
        if c == target:
            count+=1
    return count
arr=[1,2,3,2,3,2]
aim= 3
print(count_occur(arr,aim))
"""
def countNO_dup(numbers): #this gives the number of duplicates pairs
    count=0
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]== numbers[j]:
                count+=1
    return count
arr=[1,2,3,2,3,2]
print(countNO_dup(arr))
