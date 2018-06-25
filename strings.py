user_name = input('Please enter Name ')
print(user_name)

str = "Hello {name}"
str = str.format(name = "World")
print(str)

text =  "Hello World"
print(text.count('l'))
print(text.count("World"))
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.isprintable())
print(text[0])
print(text[0: 8: 2])
print(text[::-1])
print(text[-1])


email = input('Enter Email ').strip()
user = email[0: email.index('@'):1]
domain = email[email.index('@')+1::1]
print(user)
print(domain)