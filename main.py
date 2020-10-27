#Strong Password Generator Requirements
# Requires a length as per the user's suggestion. Ask the user for the length required.
# Must contain atleast 1 capital letter (A-Z)
# Must contain atleast 1 small letter (a-z)
# Must contain numeric values (0-9)
# Must conatin special characters (!@#$%^&*)

# Importing random module
import random
# Importing the string module
import string
#-------------------GLOBAL VARIABLES------------------------


# Function defined to generate password
def password_generator():

  # Taking the length of the password to be generated from the user
  max_length = int(input("Please enter the length of the password to be generated: "))


   # Creating a list to store the password
  password = []

  # Setting up the capital letters
  capital_letters = string.ascii_uppercase
  # Setting up the small letters
  small_letters = string.ascii_lowercase
  # Setting up the digits
  digits = string.digits
  # Setting up the special characters
  special_characters = string.punctuation

  # Extend function is used to add / concatenate elements directly into the list password and list() method is used to convert the string into the list and list can only be extended
  password.extend(capital_letters)
  password.extend(small_letters)
  password.extend(digits)
  password.extend(special_characters)

  # Shuffle method is used to shuffle all the characters just like we shuffle a deck of cards
  random.shuffle(password)

  print()

  #printing the password using join() method which concatinatinates all the characters with no space till the length of the max_length
  return print("Your password is: "+"".join(password[0: max_length]))

  
# Calling the function password_generator
password_generator()

 







