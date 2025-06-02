def type_converter(type_of_output): # decorator factory
    def decorator(func):  
        def wrapper(*args, **kwargs):  
            x = func(*args, **kwargs)
            result = type_of_output(x)
            print(result, type(result))
            return result
        return wrapper
    return decorator

@type_converter(str)
def return_int():
    return 5

@type_converter(int)
def return_string():
    return 'not a number'


y = return_int()
print("type(y).__name__", type(y).__name__) 
try:
   y = return_string()
   print("shouldn't get here!")
except ValueError:
   print("can't convert that string to an integer!") # This is what should