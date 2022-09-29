#Import section

from datetime import date ## This imports the data library 
import getpass ## This imports getpass for username

from employee import Employee

#Flower Box section

#####################################################################################
#
#   Name: Araceli Chavez
#   Date: 09/15/2022
#   Program Description: This program username password generator will add on and 
#   further improve our last program username generator dup checker. It will do this 
#   by testing our new function and object oriented programming logic. To start, we'll 
#   ask the user what type of password they would like with their new username using 
#   input logic to ask 3 additional questions such as "How long they want it to be, 
#   would they like special characters, and would they like numbers in it." We will 
#   then need to validate that the password length they desire is an integer between 
#   10 and 16. We will also be creating a person class file and an employee class file 
#   that will inherit the person class and add the method that will allow us to create 
#   a password for the user. In addition to this, we'll also be displaying a message
#   for each employee along with their age in years and a complete list of employee's 
#   with their first name, last name, birth year, and password among other things.      
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
employee_greeting_age_list = [] ## This sets employee greeting age list as a list  
greeting = "" ## This sets greeting as a string
age = 0 ## This sets age as a integer
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

#Input section

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
        password_length = input("Enter a number between 10 and 16: ") ## This will ask the user to enter a number between 10 and 16 and set the input as password length
        try:
            password_len_int = int(password_length) ## This converts the number the user enters for the length they want their password to be to an integer and sets it as password len int
            if(password_len_int in range(10,17)): ## This Checks to see if password len int, what length the user wants their password to be, fits our paramter between 10 and 16
                break ## If it does, it will break out
            else:
                continue ## If it doesn't it will continue to ask
        except:
            continue ## If anything is entered other than an integer it will throw them back into the loop
    
    spec_char_answer = input("Do you want special characters in your password? Yes or No? ") ## This asks the user if they want special characters in their password and sets it as spec char answer

    if spec_char_answer in YES_LIST:
        use_spec_chars = True ## If the user answers "spec char answer" (line 96) with any of the items in the YES_LIST then it will declare the variable use spec chars as true otherwise it will get treated as a no and logic will repeat the process until it gets a yes from the user 
    
    number_answer = input("Do you want numbers in your password? Yes or No? ") ## This asks the user if they want numbers in their password and sets it as number answer 

    if number_answer in YES_LIST:
        use_numbers = True ## If the user answers "number answer" (101) with any of the items in the YES_LIST then it will declare the variable use numbers as true otherwise it will get treated as a no and logic will repeat the process until it gets a yes from the user 
    
    print("You entered " + first_name + " " + last_name + " " + year_born + "\nwith Password length: " + str(password_len_int) + " \nwith Special Characters: " + spec_char_answer + " \nwith Numbers: " + number_answer + "\nis this correct? ") ## This displays a concatenating sentence for the user adding the words "You entered" with the first name, last name, year born variables, (moves to a new line) to the words "with password length: " and displaying the user's input to this, (moves to a new line) to the words "with Special Characters:" and displaying the user's input to this, (moves to a new line) to the words "with Numbers:" and displaying the user's input to this, in addition to the question "is this correct?"
    is_this_correct = input("Yes or No: ") ## This asks the user whether the concatentated sentence in line 106 using the input the user entered is correct or not, if it is correct, then to input a yes if not then input a no

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
    employee_first_name = employee[0] ## This will take employee's first name out of the employee tuple and stick it into a variable called employee first name
    employee_last_name = employee[1] ## This will take employee's last name out of the employee tuple and stick it into a variable called employee last name
    employee_year_born = employee[2] ## This will take employee's year born out of the employee tuple and stick it into a variable called employee year born
    
    username = build_username(employee_first_name, employee_last_name, employee_year_born, dup_found) ## This uses the function build username to create an employee username 

    if username in username_list: ## This tests to see if the username created in line 137 is already in the username list 
        dup_found = True ## If it is and the duplicate is found it will set the variable dup found to true
        username = build_username(employee_first_name, employee_last_name, employee_year_born, dup_found) ## This makes a call to the build username function and execute the code statement under else (line 63)
    
    username_list.append(username) ## This will then add the username to the username list

    my_employee = Employee(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]) ## This makes a copy of the Employee class to work with 
    password = my_employee.build_password() ## This goes back to the function section and builds password 
    temp_tuple = (my_employee.greet_person(), my_employee.age()) ## This declares a tuple, makes a call to greet_person in the Person class, returns that value, makes a call to age in the same Person class, returns that value, and sticks those values in the first and second positions of the tuple
    employee_greeting_age_list.append(temp_tuple) ## This takes the data out of the employee greeting age list and puts it in the temp tuple
    employee_record = [employee_first_name, employee_last_name, employee_year_born, username, password] ## This creates a list with the employee's first name, last name, year born, username, and password

    employee_data_dictionary[username] = employee_record ## This grabs employee data dictionary and puts in a key value equal to the username and pairs it to the employee record

username_sorted_list = list(username_list) ## This makes a copy of username list 

username_sorted_list.sort() ## This sorts the list 

#Output section

print(date.today()) ## This displays the user's username
print(getpass.getuser()) ## This displays today's date 

for employee_greeting_age in employee_greeting_age_list:
    greeting = employee_greeting_age[0] ## This will take the greeting from the first position in the tuple
    age = employee_greeting_age[1] ## This will take the age from the second position in the tuple
    print(greeting + " You are " + str(age) + " years old ") ## This displays a concatenated string message of greeting + the words "you are" + display the user's age + the words "years old"

print(all_employee_data_in_tuples_list) ## This displays the whole employee data list as the list is being built everytime a tuple is added
print(username_list) ## This will display the list of usernames after the program finishes going through the loop 
print(employee_data_dictionary) ## This displays the employee data dictionary 
print(username_sorted_list) ## This displays a sorted username list

for employee in all_employee_data_in_tuples_list:  
    employee_data_displayed = employee[0] + " " + employee[1] + " was born in " + employee[2] ## This sets the variable employee data displayed as a concatenation of the employee first name, last name, the words "was born in", and their year of birth all together 
    print(employee_data_displayed) ## This displays the concatenated sentence formed above in line 173 using the employee data the user entered (to form first name + last name + was born in + year born)