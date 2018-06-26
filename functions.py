
def reverse(data):
    return data[::-1]
data = input('Enter Something: ').strip()
print(reverse(data))

#scope
a = [1,2,3]
def f1():
    a[1] = [5,6,7]
    print(a)
f1()
print(a)


#parameters
def function(name, age, likes = "Python"):
    print("Hi {}. Age is {}. Likes are {}".format(name, age, likes))

function("Vivek", 25, "Cricket")
function(age = 25, name="Vivek")


#Unpacking interable
def unpacking(data):
    print(*data)
unpacking([1,2,3,4,5])
unpacking("Abc")
unpacking({"name": "Vivek", "Age": 25})

#Packing iterable  -- added to Tuple while packing -- can be used where don't know about arguments
def packing(*data):
    print(data)
packing([1,2,3,4,5])
packing("Abc")
packing({"name": "Vivek", "Age": 25})

#keyword Argument
def about(name, age, likes):
    print("Hi {}. Age is {}. Likes {}".format(name, age, likes))

data_dic = {'name': 'Vivek', 'age': 25, 'likes': 'Cricket'}
about(**data_dic)

def foo(**kwargs):
    for key, value in kwargs.items():
        print('key is {}. Value is {}'.format(key, value))

foo(name="Vivek", age= 25)