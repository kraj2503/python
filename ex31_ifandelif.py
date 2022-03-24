print("you enter a dark room with 2 doors,")
print("do you go through door #1 or door #2?")

door = input("> ")

if door == "1":
    print("there's a giant bear here eating a cheese cake")
    print("what will you do")
    print("1 take the cake.")
    print("2. scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("the bear eats your face off. good job!")
    elif bear == "2":

        print("bear eats your face off. good job!")
    else:

        print(f"""well, doing {bear} is probably better
           bear runs away""")

elif door == "2":

    print("you stare into the endless abyss at chtulhu's retina")
    print("1. blueberries")
    print("2. yello jacket clothspin.")
    print("3. understanding revolvers yelling melodies")

    insanity = input('> ')

    if insanity == "1" or insanity == "2":
        print("your body survives powered by mind of jello")
        print("good job!")
    else:
        print("the insanity rots you")
        print("good job")

else:
    print("you stumble and fall on a knife and die")
