print("Please answer a survey ")
print("How many cats are there?", end=' ')
cats = input()
print("How many people are out there", end=' ')
people = input()
print("how many dogs are out there", end=' ')
dogs = input()

if cats > people:
    print("cats are everywhere")

if cats < people:
    print("world is safe from cats")

if people == cats:
    print("critical moment b/w human and cats")

if people > dogs:
    print("dogs need more care")

if people < dogs:
    print("dogs are excess")

if people == dogs:
    print("Human and dogs are well treated")

if cats > dogs:
    print("cats are dominating over dogs")

if cats < dogs:
    print("Nice less cats are there compared to dogs")

if cats == dogs:
    print("both cats and dogs are equal")

print("Do you want to answer further (yes/no)")

answer = input()


if answer == "yes":
    print("Thanks")

    print("which one to you like more.... Dogs/cats/both/none")
    like = input('> ')

    if like == "dogs":
        print("hey dog-lover! I like you")

        print("do you have one?")

        have = input()

        if have == "yes":
            print("you are best")

        if have == "no":
            print("you should try to adopt one")
            print("thanks for survey! Have a nice day")

    if like == "cats":
        print("""hii cat-lover
        thanks for participating""")

    if like == "both":
        print("you are best..."
              "do you have one?")
# error in  no
if answer == "no":
    print("thanks for participating")

    quit()

