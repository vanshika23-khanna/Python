#Q82. Demonstrate decorator

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
say_hello()

print("\n\nThis program is executed by Vanshika Khanna , 0231BCA033")