import math
def hyp(base, height):
       val = base ** 2 + height ** 2
       return math.sqrt(val)
val1= input("enter the base ")
val2 = input("enter the height ")
try:
       num1= int(val1)
       num2 = int(val2)
except ValueError:
       print("Invalid number")

print(hyp(num1,num2))
