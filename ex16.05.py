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

output = line1 + '\n' + line2 + '\n' + line3 + '\n'

print("I'm going to write these to a file.")

target.write(output)

print("and finally we close it.")
target.close()
