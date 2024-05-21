
# You can provide default values for function parameters.
# These values are used if the caller does not specify them.

# ~ This function greets the user.
def greet(name="World"):
    print(f"Hello, {name}!")

greet()  # Output: Hello, World!
greet("Eric!")  # Output: Hello, Eric!
