def my_function():
    print("Hello from a function")
#calling a function
my_function()

#arguments
def my_func(fname):
    print(fname+" Nyamora")

my_func("Clinton")
my_func("Juma")

#arbitrary arguments
def my_Func(*kids):
    print("The youngest child is "+ kids[2])
my_Func("Emil","Tobias","Linus")
