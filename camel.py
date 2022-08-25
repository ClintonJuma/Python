camel=input("Input name in Camelcase: ")
print("Corresponding name in snake_case: ",end="")
for x in camel:
    if x.islower():
        print(x, end="")
    else:
        print("_"+x.lower(),end="")
print("")