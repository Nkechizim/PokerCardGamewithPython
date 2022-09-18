#name, adjective, noun
mad_libs = "{} laughed at the {} {}"

print(mad_libs)
print(mad_libs.format("Debby", "blue", "chicken"))

mad_libs = "{0} laughed at the {1} {2}"

print(mad_libs.format("Debby", "blue", "chicken"))

mad_libs = "{2} laughed at the {1} {0}"

print(mad_libs.format("Debby", "blue", "chicken"))

mad_libs = "{name} laughed at the {adjective} {noun}"

print(mad_libs.format(name = "Debby", adjective = "crazy", noun = "chicken"))
print(mad_libs.format(adjective = "crazy", name = "Debby", noun = "chicken"))

print()

def mad_libs(name, adjective, noun):
    mad_libs = "{name} laughed at the {adjective} {noun}"
    print(mad_libs.format(name = name, adjective = adjective, noun = noun))

name = input("Enter a name: ")
adjective = input("Enter a adjective: ")
noun = input("Enter a noun: ")

mad_libs(name, adjective, noun)
    