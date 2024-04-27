# 1 With only a print
print("1. Hello World")

# 2 With only a variable
message = '2. Hello World'
print(message)

# 3 With a function
def greetings():
    name = input('What is your name? ')
    return print(f'3. Hello World, {name}')

greetings()