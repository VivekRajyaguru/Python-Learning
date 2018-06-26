list1 = [1, 10, 5, 18, 225, 60, "Abc", "Test", True, False, [1, 2 ,3]]
print(list1.count(1))
print(list1[6])
print(list1[0: 7: 1])
print(list1[-1][1])
print(list1)
list1.insert(2, 200)
list1.insert(6, [1,2, 4])
print(list1)



users = ['Test', 'Vivek']
flag = True
while flag:
    user = input('Enter Name ').strip().capitalize()
    if user in users :
        print('Welcome {name}'.format(name = user))
        option = input('Want to Remove from System(Y/N)?').strip()
        if option.lower() == 'y':
            users.remove(user)   
            print('{name} removed from System'.format(name=user))         
        flag = False
    else: 
        print('User not Defined')
        option = input('Want to be Added to System (y/n)?').strip()
        if option.lower() == 'y':
            users.append(user)
            print('Welcome {name} to System'.format(name=user))
            flag = False   
        else:
            flag = False   
