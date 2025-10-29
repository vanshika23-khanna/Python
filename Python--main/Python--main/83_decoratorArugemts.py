#Q83. Demonstrate decorator with arguments

def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")

print("\n\nThis program is executed by Vanshika Khanna , 0231BCA033")