# # Basic class definition
# class Dog:
#     initialization method __init__() that runs automatically
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def call_dog(self):
#         print(f"Come here, {self.name}!")

#     def speak(self):
#         print("bark bark bark")

# dog1 = Dog("Spot", 2)
# dog1.call_dog()
# dog1.speak()
# print(f"dog1's name is {dog1.name}.")

# dog2 = Dog("Wally", 4)
# dog2.call_dog()
# dog2.age += 1
# print(dog2.age)

# # Expanding the class: class attributes and class methods
# class Dog:
#     # _count is a class variable
#     # it belongs to the class itself
#     # variable starts with a single underscore to signal that it’s intended for internal use

#     _count = 0  

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Dog._count += 1 

#     def call_dog(self):
#         print(f"Come here, {self.name}!")

#     def speak(self):
#         print("bark bark bark")
# # class method, declared using the @classmethod decorator
#     @classmethod
#     def get_dog_count(cls):
#         # cls (short for class)
#         return cls._count

# # Create a couple of dogs
# dog1 = Dog("Spot", 2)
# dog1.call_dog()
# dog1.speak()
# print(f"dog1's name is {dog1.name}.")

# dog2 = Dog("Wally", 4)
# dog2.call_dog()
# dog2.age += 1
# print(f"dog2's new age: {dog2.age}")

# print(f"Total dogs created: {Dog.get_dog_count()}")  


# # Class inheritance
# # class that’s similar to Dog, but with a few differences 
# class BigDog(Dog): # inherits from Dog
#     def __init__(self, name, age): 
#         # Call the parent class's __init__ to set name/age
#         super().__init__(name, age) 

#     def fetch(self):
#         print("Got it.")

#     def speak(self):
#         print("Woof Woof Woof") # overrides Dog.speak()
# # The speak_verbose() method shows how to call both the original Dog.speak() (using super()) and BigDog.speak()
#     def speak_verbose(self):
#         # call Dog.speak(), then BigDog.speak()
#         super().speak()
#         self.speak()

# dog3 = BigDog("Butch", 3)
# dog3.call_dog()
# dog3.speak()
# dog3.speak_verbose()
# print(f"Total dogs created: {BigDog.get_dog_count()}") 

# print(Dog.__dict__) # prints attributes and methods for the Dog class
# # print(dog1.__dict__) # prints the attributes of the instance and their values.


# # You can also create classes from system classes:
# class Shout(str):
# #    In this case, the subclass overrides the __new__ method of the str class, and not the __init__ method, because strings are immutable.
#    def __new__(cls, content):
#       return str.__new__(cls, content.upper())

# x = Shout("hello there")
# print(x) # prints HELLO THERE


# decorators
'''We’ve already seen some decorators like @classmethod in our class definitions. But what are these things? 
A decorator is syntactic sugar that says, “Take this function or class, and pass it through another function to modify it.” 
You will probably use decorators more than you write them in Python, so let's see them in action to see how useful they can be.'''

# # @classmethod
# # def get_dog_count(cls):
# # This tells Python: “Don’t treat get_dog_count() like a normal method. Treat it as a method that applies to the class itself.” That’s all a decorator is doing: changing the behavior of a function or method, without you having to rewrite that function.

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     @property
#     def area(self):
#         return 3.14 * self.radius ** 2

#     @property
#     def diameter(self):
#         return 2 * self.radius
    
# c = Circle(3)
# print(c.area)    
# print(c.diameter)  

# c.radios = 5
# print(c.area)
# # You didn't have to re-assign anything: area (and diamater) are always recalculated based on the current radius.

# from dataclasses import dataclass

# @dataclass
# class Book:
#     title: str
#     author: str

# book1 = Book("Dune", "Frank Herbert")
# book2 = Book("Dune", "Frank Herbert")
# book3 = Book("Neuromancer", "William Gibson")

# print(book1)
# print(book2.title)          
# print(book1 == book2) # True — same data, so considered equal
# print(book1 == book3) # False — different data

# '''There are a few things to notice about dataclass objects:

# You didn’t have to write an __init__ method or any other methods for the class: Python did it for you behind the scenes. You just declare the attribute names and their data types.
# You can access the attributes of a book object using standard dot notation (book2.title).
# You can check if two different books are the same with book1 == book2 without having to define your own __eq__() operator.'''

# Writing your own decorators
# def say_hello():
#     print("Hello!")

# def repeat_me(func, num_repeats):
#     for _ in range(num_repeats):
#         func()

# repeat_me(say_hello, 5)  # Will print "Hello!" 5x

# def my_decorator(func):
#     def wrapper():
#         print ("Hello!")
#         func()
#         print ("World!")
#     return wrapper

# @my_decorator
# def print_name():
#     print("John")

# print_name()

# # Decorator that will work with any function
# import time

# def timer(func):
#     ## Output the time the inner function takes
#     def wrapper_timer(*args, **kwargs):
#         start_time = time.perf_counter()
#         value = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         run_time = end_time - start_time
#         print (f"Finished in {run_time:.4f} secs")
#         return value
#     return wrapper_timer

# @timer
# def wait_half_second():
#     time.sleep(0.5)
#     return "Done"

# wait_half_second()

# # Decorator with arguments: decorator factories
# def repeat_with_prefix(prefix, num_repeats): # decorator factory
#     def decorator(func):  # The decorator: takes the function
#         def wrapper(*args, **kwargs):  # The wrapper: runs the function with extra behavior
#             for _ in range(num_repeats):
#                 result = func(*args, **kwargs)  # Call the original function
#                 print(f"{prefix} {result}")
#         return wrapper
#     return decorator

# @repeat_with_prefix(">>", 3)  
# def greet(name):
#     return f"Hello, {name}!"

# greet("Amanda")

# callback_dict={}

# def wrap_output(before, after,greeting_type):
#     def decorator_wrap_output(func):
#         callback_dict[greeting_type] = func
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             return before + result + after
#         callback_dict[greeting_type]=wrapper
#         return wrapper
#     return decorator_wrap_output

# @wrap_output("begin:", ":end","for_hello")
# def hello():
#     return "Hello, World!"

# @wrap_output("begin:", ":end","for_goodbye")
# def goodbye():
#     return "Goodbye, World!"

# print(callback_dict["for_hello"]()) # Will print "begin:Hello, World!:end"

# print(callback_dict["for_goodbye"]()) # Will print "begin:Goodbye, World!:end"

# #  Python List Comprehensions
# integer_list=[]
# for x in range(20):
#     integer_list.append(x)

# # with Python, you can use a list comprehension as a shorthand
# integer_list = [x for x in range(20)]
# odd_list = [x for x in range(20) if x%2 != 0]
# odd_squares_list = [x**2 for x in range(20) if x%2 !=0]
# # or
# odd_squares_list = [x**2 for x in odd_list]

# # Generator Expressions

# # A generator expression is just like a list comprehension, except that you use parentheses instead of square brackets.

# odd_squares_generator = (x**2 for x in range(20) if x%2 !=0)

# for y in odd_squares_generator:
#     print(y)


# # Python Closures
# # A Python closure is a way of wrappering information by returning a function that has access to that information.  This provides some protection for the stuff you wrapper.
# def make_secret(secret):
#     def did_you_guess(guess):
#         if guess == secret:
#             print("You got it!")
#         else:
#             print("Nope")
#     return did_you_guess

# game1 = make_secret("swordfish")
# game2 = make_secret("magic")

# game1("magic") # Prints nope
# game1("swordfish") # Prints you got it
# game2("magic") # Prints you got it

# Of course, the wrappered function could also store data, but you may need the nonlocal keyword.  This makes the variable still wrappered within the outer function, but accessible within the inner function:

# def make_secret(secret):
#     bad_guesses = 0
#     def did_you_guess(guess):
#         nonlocal bad_guesses
#         if guess == secret:
#             print("You got it!")
#         else:
#             bad_guesses+=1
#             print(f"Nope, bad guesses: {bad_guesses}")
#     return did_you_guess

# game1 = make_secret("swordfish")
# game1("magic") # Prints nope, bad guesses 1
# game1("magic") # Prints nope, bad guesses 2
