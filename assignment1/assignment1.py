def hello():
    print("Hello!")
    return "Hello!"

hello()

def greet(name):
    print(f"Hello, {name}!")
    return f"Hello, {name}!"

greet("Reviewer")

def calc(a,b, value='multiply'):
    result=None
    try:
      match value:
        case 'multiply':
          result = a * b
        case 'add':
          result = a + b
        case 'add':
          result = a + b
        case 'subtract':
          result = a - b
        case 'divide':
          result = a / b
        case 'modulo':
          result = a % b
        case 'int_divide':
          result = a // b
        case 'power':
          result = a ** b
        case _:
          raise ValueError("There is no such operator")
    except ZeroDivisionError:
      print("You can't divide by 0!")
      return "You can't divide by 0!"
    except TypeError:
      print(f"You can't {value} those values!")
      return f"You can't {value} those values!"
    else:
      print(result)
      return result

calc(3, 5)
calc(3, 5, 'add')
calc("8", 0, 'divide')


def data_type_conversion(value, type):
    converted_value = None
    try:
      match type:
        case 'int':
          converted_value = int(value)
        case 'float':
          converted_value = float(value)
        case 'str':
          converted_value = str(value)
        case _:
          raise ValueError("There is no such type")
    except ValueError:
      print(f"You can't convert {value} into a {type}.")
      return (f"You can't convert {value} into a {type}.")
    else:
      print(converted_value)
      return converted_value
  

data_type_conversion("110", "int")
data_type_conversion("5.5", "float")
data_type_conversion("banana", "int")


def grade(*args):
    try:
      result = sum(args)/len(args)
    except:
      print("Invalid data was provided.")
      return("Invalid data was provided.")
    else:
      print(result)
      if result >= 90:
        return "A"
      elif result < 90 and result >= 80:
        return "B"
      elif result < 80 and result >= 70:
        return "C"
      elif result < 70 and result >= 60:
        return "D"
      else: 
        return "F"
  
grade(75,85,95)
grade("three", "blind", "mice")


def repeat(string, count):
    newString = ""
    for _ in range(count):
      newString += string
    print(newString)
    return newString


repeat("up,", 4)


def student_scores(pos, **kwargs):
    if pos == "best":
      compareNum = 0
      name = ""
      for key, value in kwargs.items():
        if compareNum > value:
          continue
        else:
          compareNum = value
          name = key
      print(name)
      return name
    else:
        score = kwargs.values()
        print(sum(score)/len(score))
        return(sum(score)/len(score))
   
student_scores("mean", Tom=75, Dick=89, Angela=91)
student_scores("best", Tom=75, Dick=89, Angela=91, Frank=50 )


def titleize(str):
    little_words=("and", "a", "is", "an", "the", "of", "in")
    str_to_list = str.split()
    new_list = []
    for i, word in enumerate(str_to_list):
      if i == 0 or i==(len(str_to_list)-1) or word not in little_words:
        new_list.append(word.capitalize())
      else:
        new_list.append(word)
    print(" ".join(new_list))
    return " ".join(new_list)

titleize("war and peace")
titleize("after on")
titleize("a separate peace")


def hangman(secret, guess):
    secret_list = list(secret)
    guess_list=list(guess)
    new_str=""
    for letter in secret_list:
      if letter in guess_list:
        new_str += letter
      else:
        new_str += "_"
    print(new_str)
    return(new_str)

hangman("difficulty","ic")

def pig_latin(s):
    if type(s) is not str:
        return
    list_of_strings = s.split(" ")
    vowels = ("a", "e", "o", "u", "i")
    # container to save transformed words 
    modified_list = []
    for word in list_of_strings:
        
        # transform unmodified string to modified list
        str_in_list=list(word)

        def final_modification():
            # add letters when letters it the word reorganized
            str_in_list.append("ay")
            # add word as string in the list
            modified_list.append("".join(str_in_list))


        if len(str_in_list) == 1:
            final_modification()
            break

        # function to reorganize letters
        def reorganize():
            pop_letter=str_in_list.pop(0)
            str_in_list.append(pop_letter)
        
        # function to check first 2 letters and reorganize them if necessary
        def check_letters(letters):
            if letters[0] in vowels or len(letters) == 2:
                return
            if letters[0] == "q" and letters[1] == 'u':
                for _ in range(2):
                    reorganize()
            else:
                reorganize()
            # check again until return condition met
            check_letters(letters)
        # run the function with word we are checking 
        check_letters(str_in_list)

        final_modification()

    print("modified_list", " ".join(modified_list))
    # return previously created list of mew words as string
    return(" ".join(modified_list))



pig_latin("apple")
pig_latin("banana")
pig_latin("cherry")
pig_latin("quiet")
pig_latin("square")
pig_latin("the quick brown fox")
pig_latin("hug")
pig_latin("squint")
pig_latin("qu")
pig_latin("b")
pig_latin(5)
pig_latin(True)