global_variable = "i am outside function"
def my_function():
    print(global_variable)
    
my_function()
print(global_variable)