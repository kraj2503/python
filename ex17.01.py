from sys import argv
from os.path import exists

script, from_file, to_file = argv

input = open(from_file)
input = input.read()

output = open(to_file,'w')
output.write(input)

