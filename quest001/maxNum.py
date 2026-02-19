def largest_Num(numbers): # this code returns the largest number in a list
    marx= numbers[0]
    for c in numbers:
        if c > marx:
            marx=c
    return marx
arr = [4, 7, 1, 9, 3]
print(largest_Num(arr))
