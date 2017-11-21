# Program pyta użytkownika, ile elementów ma zawierać zbiór niezhashowanych kluczy.
# Następnie prosi o podanie kluczy oraz o rozmiar listy
# w której mają się znaleźć zhashowane klucze. 
# Zwraca zhashowaną lishę wedługo hashowania z adresowaniem liniowym:
# h(k) = k mod m,  gdzie k - niezhashowany klucz, m = rozmiar listy.
# Autor: Bartłomiej Pysiak

def greet():
  print("Welcome in ListHash! Here you can hash your lists.\n")
  
def ask_how_many_elements():
  while True:
    try:
      how_many = int(input("How many elements ?"))
      return how_many
    except ValueError as e:
      print("Wrong value: ", e)
      continue

def input_unhashed_elements(unhashed_collection, unhashed_size):
  while True:
    for i in range(unhashed_size):
      try:
        element = int(input("Please input unhashed element"))
        unhashed_collection.append(element)
      except ValueError as e:
        print("Wrong value:", e)
        continue
    return unhashed_collection

def create_unhashed_collection():
  unhashed_collection = []
  unhashed_size = ask_how_many_elements()
  input_unhashed_elements(unhashed_collection, unhashed_size)
  return unhashed_collection
  
def create_empty_list():
  my_list = []
  list_size = ask_how_many_elements()
  for i in range(list_size):
    my_list.append(None)
  return my_list
  
def hashing(unhashed_collection, my_list):
  hashed_list = my_list
  count = 0
  while True:
    for i in range(len(unhashed_collection)):
      while True:
        linear_addressing = ((unhashed_collection[i])%len(my_list)+count)%len(my_list)
        if hashed_list[linear_addressing] == None:
          hashed_list[linear_addressing] = unhashed_collection[i]
          count = 0
          break
        else:
          count += 1
          continue
    return hashed_list
    
def main():
  greet() 
  print("Unhashed collection: ")
  unhashed_list = create_unhashed_collection()
  my_list = create_empty_list()
  print("This is your unhashed collection: ",unhashed_list)
  print("This is the list that will contain your hashed elements: ", my_list)
  my_list = hashing(unhashed_list, my_list)
  print("Your hashed list is: ", my_list)
main()
