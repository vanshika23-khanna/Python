#Q84. Demonstrate decorator using wraps

import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello():
    """This function says hello."""
    print("Hello!")
print(say_hello.__name__)
print(say_hello.__doc__)

print("\n\nThis program is executed by Vanshika Khanna , 0231BCA033")