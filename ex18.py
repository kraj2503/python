# this is like one of your scripts with argv

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#ok that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this just make one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this one makes no argumant
def print_none():
    print("i got nothing")

print_two("Kshitiz","Raj")
print_two_again("anmol","raj")
print_one("one")
print_none()
