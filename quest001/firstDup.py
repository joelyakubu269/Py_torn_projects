def first_dup(numbers):
    # numbers = [4, 2, 1, 2, 5, 4]
    #    Expected: 2
    first_duplicate= None
    smallest_dup= len(numbers) # since we dont know the exact value ,we compare with an exclusive one
    for i in range(len(numbers)): # the outer loop
        for j in range(i+1,len(numbers)):# the inner loop
            if numbers[i] == numbers[j]: # if a duplicate is found
                if j < smallest_dup: # if its index is smaller than smallest_dup,we compare positions not values
                    smallest_dup= j # not we store positions not values
                    first_duplicate= numbers[j] # we store the value
    return first_duplicate
arr = [4, 2, 1, 2, 5, 4]
print(first_dup(arr))
# its like a race we store duplicates and check how close they are to the start

