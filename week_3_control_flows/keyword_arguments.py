# You can call functions using keyword arguments, where you explicitly specify the parameter names.
# ! This function greets the user with a custom greeting.


def greet(greeting, name):
    print(f"{greeting}, {name}!")

# Output: Hi, Eric!
greet(name="Eric", greeting="Hi")  

