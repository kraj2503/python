print("No. of people?")
people = input('> ')

print("No. of cars available?")
cars = input('> ')

print("No. of trucks?")
trucks = input('> ')


if cars > people:
    print("we should take cars")
elif cars < people:
    print("we should not take cars")
else:
    print("we cant decide")
if trucks > people:
    print("we may take trucks")
elif trucks < people:
    print("we can\'t take trucks")
else:
    print("trucks are good option")
