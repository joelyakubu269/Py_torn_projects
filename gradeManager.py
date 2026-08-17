def GradeDecider():
    name = input("what is your name ?")
    score = input("what did you score ?")
    print(name)
    print(score)
    Grade = ""
    results = {
        name: [score,Grade]
    }
    if score > 90:
        Grade = "A"
    elif score > 80 and score < 90 :
        Grade = "B"
