for item in range(1,10, 2): #start, stop, step
    print(item)

for item in [1,2,3,4]:
    print(item)

for item in "abcd":
    print(item)

vowels = 0
consonants = 0
for item in "I am Vivek Rajyaguru":
    if item.lower() in 'aeiow':
        vowels = vowels + 1
    elif item == ' ':
        pass
    else:
        consonants = consonants + 1

print(vowels)
print(consonants)


data = {
    "male": ["Test", "Dummy", "User"],
    "female": ["Admin", "Testing", "ABC"] 
}
for item in data.keys():
    for name in data[item]:
        if "a" in name or "A" in name:
            print(name)


even_number = [x for x in range(1, 101) if x %2 ==0]
odd_number = [x for x in range(1, 101) if x %2 !=0]
print(even_number)
print(odd_number)

words = ["Hello", "Test", "World", "Dog", "User", "List"]
print([[w, len(w), w.upper(), w.lower()] for w in words if 'o' in w or 'O' in w])


# project

while True:
    data = input('Enter Something: ').strip().lower()    
    words = data.split()
    new_data = []
    for item in words:
        if item[0] in 'aeiou':
            item = item + 'yay'
            new_data.append(item) 
        else:
            vowel_pos = 0
            for letter in item:
                if letter not in 'aeiou':
                    vowel_pos = vowel_pos + 1
                else:
                    break
            const = item[vowel_pos:] + item[:vowel_pos] + 'ay'
            new_data.append(const)
    
    print(" ".join(new_data))

