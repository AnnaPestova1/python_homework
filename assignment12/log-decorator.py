# one time setup
import logging


logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func()
        logger.log(logging.INFO, f"func.__name__: {func.__name__}, positional parameters: {args or None}, keyword parameters: {kwargs or None}, return: {result}")
        return result
    return wrapper

@logger_decorator
# Declare a function that takes no parameters and returns nothing. Maybe it just prints "Hello, World!". Decorate this function with your decorator.
def no_params():
    return 'Hello World'

@logger_decorator
# Declare a function that takes a variable number of positional arguments and returns True. Decorate this function with your decorator.
def positional_args():
    return True

@logger_decorator
# Declare a function that takes no positional arguments and a variable number of keyword arguments, and that returns logger_decorator.
def keyword_args():
    return logger_decorator 

# call functions
no_params()
positional_args(1,2,3)
keyword_args(a=1, b=2, c=3)

