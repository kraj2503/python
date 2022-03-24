from sys import exit

def gold_room():
    print(" this room is full of gold. how much do you take")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("you are greedy")


def bear_room():
    print("there is a abear here")
    print("the bear has a bunch of honey")
    print("the fat bear is in the front of another door")
    print("how are you going to move bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("the bear looks at you and slaps your face off")
        elif choice == "taunt bear" and not bear_moved:
            print("the bear has moved from the door")
            print("you can go through it now")
            bear_moved = True

        elif choice == "taunt bear" and bear_moved:
            dead("the bear gets pissed off and chew your leg off")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I have no idea what that means")


def chalu_room():
    print("here you see the great evil chalu")
    print("he ,  it, whatever stares at you and you go home")
    print("do you flee for your life or eat your head?")
    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead ("well that was tasty ")
    else:
        chalu_room()


def dead(why):
     print(why, "good job")
     exit(0)


def start():
    print(" you are in  a dark room ")
    print("there is a door on your right and left")
    print("which one will you choose")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        chalu_room()
    else:
        dead("you stumble around your room until you starve")

start()


