def cali():
        print("hello im cali a simple calculator")
        num1 = int(input("pick a number? "))
        print("Now select a number representing the operation you want to carry out")
        opr= int(input("1.(*), 2(+),3(/)"))
        num2 = int(input("pick a second number? "))
        print(num1)

        print(num2)
        result = 0
        if opr == 1 :
            result = num1 * num2
        elif opr == 2 :
            result = num1 + num2
        elif opr == 3 :
            result = num1 / num2
        else :
            print("operator is not valid")

        print(result)
cali()
