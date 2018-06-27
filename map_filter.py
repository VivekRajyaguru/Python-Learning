seq = range(0,11)

def sqr(num): return num*2

cube = lambda num: num*3

even_filter = lambda num: num%2 == 0

print(list(map(sqr , seq)))
print(list(map(cube , seq)))

print(list(filter(lambda num: num%2 !=0, seq)))
print(list(filter(even_filter, seq)))