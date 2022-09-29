#Import section

from datetime import date ## This imports the data library 
import getpass ## This imports getpass for username
import random ## This imports the random module
import json ## This imports the whole json library 

#from employee import Employee

#Flower Box section

#####################################################################################
#
#   Name: Araceli Chavez
#   Date: 09/20/2022
#   Program Description: This program username password generator error fileio 
#   will continue to add on and further improve our last program username password
#   generator. It will do this by adding error logic to our program, use try except 
#   blocks, and add descriptive messages for the user if they run into an error. 
#   These messages will let them know they ran into an error and to try again. In 
#   addition to this, we'll be working flat text files into our program. These will 
#   allow us to store and retrieve our employee data that has been stored in our 
#   dictionary file. Along with adding more logic for validating our data to our user 
#   input we will also be introducing the JSON library and Recursion in this program.       
#   
#####################################################################################

#Variables section

#Old variables
first_name = '' ## This sets first name as a variable
last_name = '' ## This sets last name as a variable
year_born = '' ## This sets year born as a variable

is_this_correct = '' ## This sets is this correct as a variable 

all_employee_data_in_tuples_list = [] ## This sets all employee data in tuples list as a list 

username_list = [] ## This sets username list as a list 

username_sorted_list = [] ## This sets username sorted list as a list 

employee_data_dictionary = {} ## This sets employee data dictionary as a dictionary  

#New variables
password_length = "" ## This sets password length as a string 
use_spec_chars = False ## This sets use spec chars as a boolean
use_numbers = False ## This sets use numbers as a boolean
dup_found = False ## This sets dup found as a boolean
YES_LIST = ["Yes", "YES", "Y", "yes", "y"] ## This sets yes list as a constant if the user answers with any of these then its correct otherwise will get treated as a no and logic will repeat the process until it gets a yes from the user

#Functions section

## This function will build a username (using the parameters first, last, year, and dup), if no duplicate username is found it will execute the code in line 61 but if a duplicate is found it will execute the code in line 63
def build_username(first, last, year, dup):
    if not dup: 
        username = first[0].lower() + last.lower() + year[-2:]
    else: 
        username = first.lower() + last[0].lower() + year[-2:]
    
    return username

## This function uses constants and variables to go get values to build our password
def build_password(password_length, use_special_characters, use_numbers):
        ALPHABET = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        SPECIAL_CHARACTERS = "!@#$%^&*"
        NUMBERS = "0123456789"
        count = 0
        password = ""

        ## This loop will iterate until it reaches the password length the user entered so if the count is less than the password length the user entered it will go through all the characters in the function build password and grabs a character from the string ALPHABET using the randomNumber variable and updates the password variable with it then clears the pwChar and increments the count variables if this logic is followed  
        while count < password_length:
            randomNumber = random.randrange(0,51,1)
            pwChar = ALPHABET[randomNumber]
            password = password + pwChar
            pwChar = ""
            count = count + 1

            ## If the user asks for special characters and the count has not exceeded the length of the password this grabs a character from the string SPECIAL CHARACTERS using the randomNumber variable and updates the password variable with it then clears the pwChar and increments the count variables if this logic is followed  
            if use_special_characters and count < password_length:
                randomNumber = random.randrange(0,7,1)
                pwChar = SPECIAL_CHARACTERS[randomNumber]
                password = password + pwChar
                pwChar = ""
                count = count + 1

            ## If the user asks for numbers and the count has not exceeded the length of the password this grabs a character from the string NUMBERS using the randomNumber variable and updates the password variable with it then clears the pwChar and increments the count variables if this logic is followed  
            if use_numbers and count < password_length:
                randomNumber = random.randrange(0,9,1)
                pwChar = NUMBERS[randomNumber] 
                password = password + pwChar
                pwChar = ""
                count = count + 1

        return password ## This returns the password wherever it was called in our main program

#Input section
try:
    with open("employee_data_dictionary.txt", "r", encoding="utf-8") as file: ## This takes whatever is in this file, make it readable, convert it to utf-8, and stick it into the variable file
        for line in file:
            temp_dict = str(line) ## This will convert line to a string
            temp_dict = temp_dict.strip() ## This will return a copy of the string and remove any leading and trailing whitespace from it
            temp_dict = temp_dict.replace("\'", "\"") ## This will replace the single tick with double ticks
            employee_data_dictionary = json.loads(temp_dict) ## This will load the JSON file and convert it to a dictionary 
except FileNotFoundError:
    print("File not found. Try again.") ## This will display the message "File not found. Try again." if the file is not found 
else:
    file.close() ## This will close the file

while len(all_employee_data_in_tuples_list) < 5: ## This uses the length in the employee tuple list to allow the user to enter the first name, last name, and year of birth for 5 employees (the iteration will continue until there are 5 sets of employee data)
    first_name = input("Enter an employee first name: ") ## This sets the first name variable to what the user enters as an employee first name
    while len(first_name) < 2: ## This sets the length of the first name the user enters to be less than 2
        first_name = input("Enter an employee first name: ") ## This sets the first name variable to what the user enters as an employee first name
        break ## If user inputs a first name when asked it will continue with logic if not it will repeat and ask the user again for a first name
    
    last_name = input("Enter an employee last name: ") ## This sets the last name variable to what the user enters as an employee last name
    while len(last_name) < 2: ## This sets the length of the last name the user enters to be less than 2 
        last_name = input("Enter an employee last name: ") ## This sets the last name variable to what the user enters as an employee last name
        break ## If user inputs a last name when asked it will continue with logic if not it will repeat and ask the user again for a last name
    
    year_born = input("Enter an employee year of birth: ") ## This sets the year born variable to what the user enters as an employee year of birth 
    while len(year_born) < 4: ## This sets the length of the year of birth the user enters to be less than 4
        year_born = input("Enter an employee year of birth: ") ## This sets the year born variable to what the user enters as an employee year of birth 
        break ## If user inputs a year of birth when asked it will continue with logic if not it will repeat and ask the user again for a year of birth 

    while True:
        password_length = input("Enter a number between 6 and 10 or 16: ") ## This will ask the user to enter a number between 10 and 16 and set the input as password length
        try:
            password_len_int = int(password_length) ## This converts the number the user enters for the length they want their password to be to an integer and sets it as password len int
            if(6 <= password_len_int <= 10 or password_len_int == 16 ): ## Only if the first condition is false will it look at the second condition ## This Checks to see if password len int, what length the user wants their password to be, fits our paramter between 10 and 16
                break ## If it does, it will break out
            else:
                continue ## If it doesn't it will continue to ask
        except:
            continue ## If anything is entered other than an integer it will throw them back into the loop
    
    spec_char_answer = input("Do you want special characters in your password? Yes or No? ") ## This asks the user if they want special characters in their password and sets it as spec char answer

    if spec_char_answer in YES_LIST:
        use_spec_chars = True ## If the user answers "spec char answer" (line 137) with any of the items in the YES_LIST then it will declare the variable use spec chars as true otherwise it will get treated as a no and logic will repeat the process until it gets a yes from the user 
    
    number_answer = input("Do you want numbers in your password? Yes or No? ") ## This asks the user if they want numbers in their password and sets it as number answer 

    if number_answer in YES_LIST:
        use_numbers = True ## If the user answers "number answer" (142) with any of the items in the YES_LIST then it will declare the variable use numbers as true otherwise it will get treated as a no and logic will repeat the process until it gets a yes from the user 
    
    print("You entered " + first_name + " " + last_name + " " + year_born + "\nwith Password length: " + str(password_len_int) + " \nwith Special Characters: " + spec_char_answer + " \nwith Numbers: " + number_answer + "\nis this correct? ") ## This displays a concatenating sentence for the user adding the words "You entered" with the first name, last name, year born variables, (moves to a new line) to the words "with password length: " and displaying the user's input to this, (moves to a new line) to the words "with Special Characters:" and displaying the user's input to this, (moves to a new line) to the words "with Numbers:" and displaying the user's input to this, in addition to the question "is this correct?"
    is_this_correct = input("Yes or No: ") ## This asks the user whether the concatentated sentence in line 147 using the input the user entered is correct or not, if it is correct, then to input a yes if not then input a no

    if(is_this_correct in YES_LIST): ## If the user says it is correct the data will be added to the list otherwise it will iterate until it is 
        employee_data = (first_name, last_name, year_born, password_len_int, use_spec_chars, use_numbers) ## This creates a tuple with the inputs of data the user entered into the variables for first name, last name, year born, password len int, use spec chars, and use numbers
        all_employee_data_in_tuples_list.append(employee_data) ## This loops through the all employee data in tuples list and creates a tuple called employee data
        first_name = '' ## If it is correct, after adding the employee first name to the list, this clears the first name variable for next iteration
        last_name = '' ## If it is correct, after adding the employee last name to the list, this clears the last name variable for next iteration 
        year_born = '' ## If it is correct, after adding the employee year of birth to the list, this clears the year born variable for next iteration
        password_length = "" ## If it is correct, it sets the variable back to default
        password_len_int = 0 ## If it is correct, it sets the variable back to default
        use_spec_chars = False ## If it is correct, it sets the variable back to default
        use_numbers = False ## If it is correct, it sets the variable back to default
    else:
        first_name = '' ## If it's not correct, this clears the first name variable for next iteration
        last_name = '' ## If it's not correct, this clears the last name variable for next iteration
        year_born = '' ## If it's not correct, this clears the year born variable for next iteration
        password_length = "" ## If it is correct, it sets the variable back to default
        password_len_int = 0 ## If it is correct, it sets the variable back to default
        use_spec_chars = False ## If it is correct, it sets the variable back to default
        use_numbers = False ## If it is correct, it sets the variable back to default
        continue ## If the user says it's not correct it will go back to the top of the loop and ask them again


#Processing section

for employee in all_employee_data_in_tuples_list:
    dup_found = False ## This method (lines 175-177 & 181) will be used to build a employee username and lines 179-180 will be used to build a password if no dup is found 
    employee_first_name = employee[0] ## This will take employee's first name out of the employee tuple and stick it into a variable called employee first name
    employee_last_name = employee[1] ## This will take employee's last name out of the employee tuple and stick it into a variable called employee last name
    employee_year_born = employee[2] ## This will take employee's year born out of the employee tuple and stick it into a variable called employee year born
    employee_password_length = employee[3] ## This will take the employee's answer of how long they want their password to be and stick it into a variable called employee password length
    employee_wants_special_characters = employee[4] ## This will take the employee's answer of whether they want to use special characters or not and stick it into a variable called employee wants special characters
    employee_wants_numbers = employee[5] ## This will take the employee's answer of whether they want to use numbers or not and stick it into a variable called employee wants numbers
    username = build_username(employee_first_name, employee_last_name, employee_year_born, dup_found) ## This uses the function build username to create an employee username 

    if username in username_list: ## This tests to see if the username created in line 181 is already in the username list 
        dup_found = True ## If it is and the duplicate is found it will set the variable dup found to true
        username = build_username(employee_first_name, employee_last_name, employee_year_born, dup_found) ## This makes a call to the build username function and execute the code statement under else (line 58)
    
    username_list.append(username) ## This will then add the username to the username list

    password = build_password(employee_password_length, employee_wants_special_characters, employee_wants_numbers) ## This goes back to the function section and builds password 
    employee_record = [employee_first_name, employee_last_name, employee_year_born, username, password] ## This creates a list with the employee's first name, last name, year born, username, and password

    employee_data_dictionary[username] = employee_record ## This grabs employee data dictionary and puts in a key value equal to the username and pairs it to the employee record

username_sorted_list = list(username_list) ## This makes a copy of username list 

username_sorted_list.sort() ## This sorts the list 

try:
    with open("employee_data_dictionary.txt", "w") as file: ## This takes whatever is in this file, make it writeable, and sticks it into the variable file
        file.write(str(employee_data_dictionary)) ## This converts the data in employee data dictrionary into a string and inserts it in a single line in the text file
except FileNotFoundError:
    print("File not found. Try again.") ## This displays the message "File not found. Try again." if the file is not found
else:
    file.close() ## This closes the file 

#Output section

print(date.today()) ## This displays the user's username
print(getpass.getuser()) ## This displays today's date 

print(all_employee_data_in_tuples_list) ## This displays the whole employee data list as the list is being built everytime a tuple is added
print(username_list) ## This will display the list of usernames after the program finishes going through the loop 
print(employee_data_dictionary) ## This displays the employee data dictionary 
print(username_sorted_list) ## This displays a sorted username list

for employee in all_employee_data_in_tuples_list:  
    employee_data_displayed = employee[0] + " " + employee[1] + " was born in " + employee[2] ## This sets the variable employee data displayed as a concatenation of the employee first name, last name, the words "was born in", and their year of birth all together 
    print(employee_data_displayed) ## This displays the concatenated sentence formed above in line 217 using the employee data the user entered (to form first name + last name + was born in + year born)