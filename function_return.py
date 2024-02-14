def hello_world():
    return 'Hello World!'

hello_world()  # returns empty bcz we are just returning the value and not printing the value.

print(hello_world())
print(hello_world().upper())

# the above example is just like len() function only with print(len('abc'))
# it will print the value otherwise with just len('abc') it will just return the value

def number_game():
    return 25

number_game()
print(number_game())