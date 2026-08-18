def cali():
        num1 = int(input("pick a number? "))
        opr= int(input("1.(*), 2(+),3(/)"))
        num2 = int(input("pick a second number? "))
        print(num1)
        print("Now select a number representing the operation you want to carry out")
        print(num2)
        result = 0
        if opr == 1 :
            result = num1 * num2
