#Q80. Global variable with nested function

global_var = "I am global"

def outer_function():
    global global_var

    def inner_function():
        global_var = "I am modified in inner"
        print(global_var)
    inner_function()

outer_function()
print(global_var)

print("\n\nThis program is executed by Vanshika Khanna , 0231BCA033")