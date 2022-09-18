def mad_libs(name, adjective, noun):
    mad_libs = f"{name} laughed at the {adjective} {noun}"
    print(mad_libs)
    mad_libs = F"{name} laughed at the {adjective} {noun}"
    print(mad_libs)

name = input("Enter a name: ")
adjective = input("Enter a adjective: ")
noun = input("Enter a noun: ")

mad_libs(name, adjective, noun)

print(f"2+2 is { 2 + 2 }")