def length(word):
    return len(word)

print(length(word = "Hello"))
print(length("Hello"))

def collect_keywords(**kwargs):
    print(kwargs)
    print(type(kwargs))

collect_keywords(a=3, b=5, c=9)
collect_keywords(a=3, b=5, c=9, d=7, y=4)
collect_keywords(a=3, y=4)

def args_and_kwargs(a, b , *args, **kwargs):
    print(f"The sum of your regular arguments are {a+b}")
    print(f"The sum of your tuple arguments are {sum(args)}")
    print(f"The sum of your dictionary arguments are {sum(kwargs.values())}")

args_and_kwargs(1,2,3,4,5,6, h=7, i=8, j=9)