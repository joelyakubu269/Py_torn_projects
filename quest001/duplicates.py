"""python
def dup_licates(word): # two pointer approach
    left=0
    right=len(word)-1
    res=[] # used list because strings are immutable hence reducing space complexity
    while left< right:
        if word[left] == word[right]:
            res.append(f"duplicates of {word[left]}  at {left} found at {right} ")
        right-=1
        if right== left:
            left+=1
            right= len(word)-1
    return "\n".join(res) if res else "no duplicates found"
print(dup_licates("nnamani"))
# downsides of this approach is readability and manual complicated workflow although
# its space time complexity is the same for nested loops
"""
def dup_licates(word):
    res=[]
    for i in range(len(word)):
       for j in range(i+1,len(word)):
           if word[j] == word[i]:
               res.append(f"duplicates of {word[j]}  at {j} found at {i} ")
    return "\n".join(res) if res else "no duplicates"
print(dup_licates("nnamani"))
# cleaner approach with no manual monitoring of when right reaches left