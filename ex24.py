print("let's practice everything.")
print('you\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tthehdfhdfhh
erhedfhfhbfd
hgdn
d
rtjgherndk,ujghdflxkugj.hdnflkugj.hvdnfhjb,dm\ndj
sd
jndf
jndf
sdfhb
\n\t\twfggrheadhdfxhfg
"""

print("-------")
print(poem)
print("_______")

five = 10-2+3-6
print(f"this should be five: {five}")


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("with a starting point: {}".format(start_point))
print(f"we'd have {beans} beans, {jars} jars, and {crates} crates")

start_point = start_point / 10

print("we can also do this way")
formula = secret_formula(start_point)

print("we'd have {} beans {} jars,{} crates.".format(*formula))
