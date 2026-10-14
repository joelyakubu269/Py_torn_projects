def seth(vals):
    for i, v in vals:
        for x, j in vals:
            if v==j and x!== i:
                vals.remove(v)
    return vals
student_ids = [1234, 5678, 1234, 1001, 1001, 1234]

res= seth(student_ids)
print(res)