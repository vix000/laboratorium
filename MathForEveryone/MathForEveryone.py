from functools import reduce
import sys

def greet():
  print(
    """
    Welcome in this program!
    
    What do you want me to do? . . .
    
    1 - Numbers
    2 - Lists
    3 - Functions
    4 - Exit
    
    """
    )
    
def make_a_choice(choice):
  while True:
    try:
      choice = int(input("Your choice?"))
      return choice
    except ValueError as ve:
      print("Value error: ", ve)
      continue
    
def input_number():
  try:
    number = int(input("Input number: "))
    return number
  except ValueError as e:
    print("Error: ", e)
  
def menu_numbers():
  print("Here you can do operations on numbers.\n")
  number = input_number()
  print("Your number is:", number)
  print(
  """
  What do you want me to do? . . .
  
  1 - Check if number is prime
  2 - ...
  3 - ...
  4 - Exit
  
  """
  )

  options = {
           1:check_if_prime,
           #2:menu_lists,
           #3:menu_math_functions
           4:menu_exit
          }
  choice = None
  choice = make_a_choice(choice)
  options[choice](number)
  
def menu_exit():
  print("Shutting down.")
  sys.exit()
  
  
def menu():
  """Uses dictionaries to represent option menu"""
  greet()
  options = {
             1:menu_numbers,
             #2:menu_lists,
             #3:menu_math_functions
             4:menu_exit
            }
  choice = None
  choice = make_a_choice(choice)
  while True:
    try:
      options[choice]()
      break
    except KeyError as ke:
      print("Key error: ", ke)
      choice = make_a_choice(choice)

def return_a_list():
  some_list = []
  while True:
    try:
      number_of_elements = int(input("Specify how many elements of a list: "))
      for i in range(number_of_elements):
        list_item = int(input("Enter an element: "))
        some_list.append(list_item)
    except ValueError as e:
      print("Err: ", e)
      some_list = []
      continue
    return some_list


def check_if_prime(num):
  if num > 1:
    for i in range(2, num):
      if num%i==0:
        return False
    else:
      print(num)
  else:
    return False

#for item in some_list:
#  check_if_prime(item)


#example_list =return_a_list()
#print(example_list)

class Find_Max():
  def __init__(self, list_arg):
    self.list_arg = list_arg
    print("Max value: ",reduce(lambda a,b: a if a>b else b, list_arg))

class Find_Min():
  def __init__(self, list_arg):
    self.list_arg = list_arg
    print("Min value: ",reduce(lambda a,b: a if a<b else b, list_arg))

def main():
  menu()
  #...
main()