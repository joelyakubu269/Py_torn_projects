def shout_out(num,message):
    if num > 10:

        return "you are too loud"
    for _ in range(num):
        print(message.upper())
    print("done")
print(shout_out(100,"joel"))
