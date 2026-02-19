def smallest_Num(numbers):
    min= numbers[0]
    for c in numbers:
        if c < min :
            min = c
    return min
arr = [4, 7, 1, 9, 3]
print(smallest_Num(arr))
