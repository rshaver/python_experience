####-----------------------00. FUNCTION GRAVEYARD  ----------------------

def is_palindrome(f):
  i = 0
  while i < len(f) / 2:
    if f[i] != f[len(f) -1 -i]:
      return False
    i += 1
  return True



def make_palindrome():
  if include_or_exclude == "Y" or include_or_exclude == "y":
    a = ""
    x = len(user_input)
    while(x >= 1):
      a += user_input[x - 1]
      x -= 1
    return a   
      
  elif include_or_exclude == "N" or include_or_exclude == "n":
    a = ""
    x = len(user_input) - 1
    while(x >= 1):
      a += user_input[x - 1]
      x -= 1
    return a 

  



#### -----------------------0. MENU  ----------------------

choice = 1
while ((choice == 1) or (choice == 2) or (choice == 3)):
  print ()
  print ("-------------------------------")
  print ("Main Menu:")
  print ("1. Is it a palindrome?")
  print ("2. Make me a palindrome!")
  print ("3. Quit.")
  print ("-------------------------------")
  print()
  
  choice = int(input("Choose a function: "))
  
  
  while (choice > 3) or (choice <=0):
    choice = int(input("Please input integer between 1-3: "))



#### ----------------------1. IS IT A PALINDROME?  ----------------------

  if choice == 1:
    user_original_phrase = (input("Please enter a phrase: "))
    de_cased = user_original_phrase.upper()
    stripped = de_cased.strip( )
    no_spaces = stripped.replace(" ", "")
    no_spaces_quote = no_spaces.replace("'", "")
    no_spaces_quote_period = no_spaces_quote.replace(".", "")
    no_spaces_quote_period_comma = no_spaces_quote_period.replace(",", "")
    no_spaces_quote_period_comma_question = no_spaces_quote_period_comma.replace("?", "")
    final_strip = no_spaces_quote_period_comma_question.replace("!", "")
    #in hinsight isalpha() would have been much easier

    if is_palindrome(final_strip):
      print(str(user_original_phrase) + " is a palindrome!")
    else:
      print(str(user_original_phrase) + " is not a palindrome. SAD.")






#### ----------------------2. MAKE ME A PALINDROME!  ---------------------- 
  
  if choice == 2:
    user_input = (input("Please enter a phrase: "))
    include_or_exclude = input("Repeat last letter? (Y/N): ")

    reverse = make_palindrome()
    print(user_input + reverse)
  
      
#### ----------------------3. QUIT. ----------------------
  
  if choice == 3:
    break
