#Import section

from datetime import date ## This imports the data library
import getpass ## This imports getpass for username

#Flower Box section

###########################################################################
#
#   Name: Araceli Chavez
#   Date: 08/25/2022
#   Program Description: 
#   
#   This hello world program allows the user to enter their name and 
#   a farenheit degree of their choosing. It will then take the user's 
#   information that they inputted and convert their first name in 
#   different formats. This inlcudes their name formatted in uppercase, 
#   lowercase, and title format. Returning only the first and last 
#   character of their name. Returning the number length of their name, 
#   splicing it, and even returning their name ten times. It also converts 
#   the user's degrees from farenheit to celsius among some other things.
#
############################################################################

#Variables section

name = '' ## This sets and declares the name variable
farenheit = '' ## This sets and declares the farenheit variable

#Input section

print('Enter your first name for a message.') ## This asks the user in a message to enter their first name 
name = input('Enter name') ## This allows the user to enter their first name 
farenheit = input('Enter a degreee to convert:') ## This allows the user to enter a degree to convert 

#Processing section

farenheit = float(farenheit) ## This converts the farenheit variable into a floating point number 

name_upper = name.upper() ## This sets name.upper as a variable that converts all the characters in a name to an uppercase format
name_lower = name.lower() ## This sets name.lower as a variable that converts all the characters in a name to a lowercase format
name_title = name.title() ## This sets name.title as a variable that converts all the characters in a name to a title format
name_len = str(len(name)) ## This takes the name the user emters and returns an integer which is the length of the string
first_character_name = name[1] ## This takes the name the user enters and returns only the first character of their name
last_character_name = name[-1] ## This takes the name the user enters and returns only the last character of their name
use_len_name_slice = name[1:len(name)] ## This take the name the user eneters and slices its length
name_fstring = f"Hello{name_title}, your name is {name_len} characters long!" ## This takes the variable "name_title" and inserts it into the string "Hello" continuing with the name_len variable and inserting it into the string "your name is___characters long!" (similar to concatenation)
name_concatenation = "Hello" + name_title + ", your name is " + name_len + " characters long!" ## This respectively adds the string "Hello", the user's name entered, the string "your name is", the length of the user's name entered, and the string "characters long!" all together
name_ten_times = name * 10 ## This takes the name the user enters and returns it ten times 
 
farenheit_int = int(farenheit) ## This converts farenheit into an integer
celsius_int = (farenheit_int -32) * 5 // 9 ## This formula takes the farenheit integer of the degree the user enters and converts it to a celsius integer
celsius_float = (farenheit_int -32) * 5 / 9 ## This formula takes the farenheit integer of the degree the user enters and converts it to a celsius floating point number 

#Output section

print(date.today()) ## This prints today's date 
print(getpass.getuser()) ## This prints the user's username

print(name) ## This prints the user's name
print(type(name)) ## This prints the class type of the name the user enters 
print(name_upper) ## This prints the user's name in an uppercase format
print(name_lower) ## This prints the user's name in a lowercase format
print(name_title) ## This prints the user's name in a title format
print(name_len) ## This prints the length of the user's name
print(first_character_name) ## This prints the first character of the user's name 
print(last_character_name) ## This prints the last character of the user's name
print(use_len_name_slice) ## This prints the name the user enters after its length is sliced
print(name_fstring) ## This prints the string statement "Hello(name_title), your name is (name_len) characters long!" replacing the variables "name_title" and "name_len" with the user's inputted information
print(name_concatenation) ## This prints the string statement "Hello (name_title), your name is (name_len) characters long!" 
print(name_ten_times) ## This prints the user's name ten times 
print(celsius_float) ## This prints the user's degree entered as a celsius floating number (found on line 53)
print(type(celsius_float)) ## This prints the class type of the celsius floating number (found on line 53) 
print(celsius_int) ## This prints the converted farenheit degree as a celsius degree in integer format (found on line 52)
print(type(celsius_int)) ## This prints the class type of the celsius degree integer (found on line 52)