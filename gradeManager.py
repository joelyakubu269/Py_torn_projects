def GradeDecider():
    name = input("what is your name ?")
    score = int(input("What did you score? "))
    print(name)
    print(score)
    Grade = ""

    if score > 90:
        Grade = "A"
    elif score > 80 and score < 90 :
        Grade = "B"
    elif  score > 70 and score < 80:
        Grade = "C"
