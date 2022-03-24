the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'prears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loops goes through a list
for number in the_count:
    print(f"this is count {number}")
#same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

#also we can go through mixed lists too
#notice we have to use {} since we dont know whats in it

for i in change:
    print(f"I got {i}")

# we can also buid lists, first try with empty one
elements = []

#then use range function to do 0to 5 counts
for i in range(0, 6):
    print(f"adding {i} to list.")
    #append is a function thatlists understand
    elements.append(i)

#now we can print them out
for  i in elements:
    print(f"element was: {i}")
