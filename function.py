
# default Function
def my_function():
    print ('Hello World')

# function with Arguments
def my_functionWithArg(arg1, arg2):
    print ('This is Arg1', arg1, ' This is Arg2', arg2);

# function with Default Arguments
def my_default_Fn(arg1="arg1", arg2="arg2"):
    print ('This is Arg1', arg1, 'This is Arg2', arg2);

# infinite Arguments

def infiniteArgs(*args):
    for item in args:
        print (item);

# function with Return Value
def sum(arg1, arg2):
    return arg1+arg2;

my_function()
my_functionWithArg("Vivek", 2)
my_default_Fn()
my_default_Fn(arg1=1, arg2=2)
infiniteArgs("Test1","Vivek","Test2")
print('Sum ', sum(10,20))