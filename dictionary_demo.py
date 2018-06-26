
data = {'people': 'Vivek', 'age': 25, 'city': 'Ahmedabad'}
data['people'] = {'name': 'Test'}
print(data)
print(data['people']['name'])


# Project

movies = {'Movie 1': [10, 2],'Movie 2': [18, 1], 'Movie 3': [25, 3]}
flag = True
print(movies.keys())
while flag:
    choice = input('What Movie u want to watch?').strip().title()
    if choice in movies:
        age = int(input('Enter Age: ').strip())
        if age >= movies[choice][0]:
            if movies[choice][1] > 0:
                movies[choice][1] = movies[choice][1] - 1
                print('Enjoy Movie')
            else:
                print('No Tickets Left')
        else:
            print('Not Allow to Watch Movie')
            flag = False
    else: 
        print('Movie No Found')
        flag = False

