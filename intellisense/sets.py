def seth(val):
    i=0
    new= []
    while i< len(val):
        j=0
        while j< len(new) and new[j] != val[i]:
            j+=1
            if j== len(new):
                new.append(val[i])
        i+=1
    return new
student_ids = [1234, 5678, 1234, 1001, 1001, 1234]

