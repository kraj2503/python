from sys import argv

script, filename = argv

print(f"we're going to erase {filename}.")
print("if you don't want that hit CTRL-C (^C).")
print("if you do want that hit RETURN.")

input("?")

print("opening the file...")
target = open(filename, 'w')

print("Truncating the file. goodbye!")
target.truncate()

print("Now I am going to ask you  for three lines")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to a file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally we close it.")
target.close()
