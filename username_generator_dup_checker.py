#Import section

from datetime import date ## This imports the data library 
import getpass ## This imports getpass for username

#Flower Box section

#####################################################################################
#
#   Name: Araceli Chavez
#   Date: 09/06/2022
#   Program Description: This program adds on and improves our last program
#   username generator. It will do this by asking the user for their first 
#   name, last name, and year born. After taking the user's inputted data the
#   program will check whether the user's data is valid with the use of while 
#   loops and force the user to enter the correct data if anything is incorrect.
#   In addition to this, the program will also use the if else logic to remove 
#   any duplicates from the username list by altering the duplicate usernames if 
#   found. 
#
#####################################################################################

#Variables section

first_name = '' ## This sets first name as a variable
last_name = '' ## This sets last name as a variable
year_born = '' ## This sets year born as a variable

is_this_correct = '' ## This sets is this correct as a variable 

all_employee_data_in_tuples_list = [] ## This sets all employee data in tuples list as a list 

username_list = [] ## This sets username list as a list 

username_sorted_list = [] ## This sets username sorted list as a list

employee_data_dictionary = {} ## This sets employee data dictionary as a dictionary

YES_LIST = ["Yes", "YES", "Y", "yes", "y"] ## This sets yes list as a constant if the user answers with any of these then its correct otherwise will get treated as a no and logic will repeat the process until it gets a yes from the user

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

    print("You entered " + first_name + " " + last_name + " " + year_born + " " + "is this correct? ") ## This displays a concatenating sentence for the user adding the words "You entered" with the first name, last name, year born variables, and the question "is this correct?"
    is_this_correct = input("Yes or No: ") ## This asks the user whether the concatentaed sentence in line 57 using the data the user entered is correct or not, if it is correct, then to input a yes if not then input a no

    if(is_this_correct in YES_LIST): ## If the user says it is correct the data will be added to the list otherwise it will iterate until it is 
        employee_data = (first_name, last_name, year_born) ## This creates a tuple with the three inputs of data the user entered into the variables for first name, last name, and year born
        all_employee_data_in_tuples_list.append(employee_data) ## This loops through the all employee data in tuples list and creates a tuple called employee data
        first_name = '' ## If it is correct, after adding the employee first name to the list, this clears the first name variable for next iteration
        last_name = '' ## If it is correct, after adding the employee last name to the list, this clears the last name variable for next iteration 
        year_born = '' ## If it is correct, after adding the employee year of birth to the list, this clears the year born variable for next iteration
    else:
        first_name = '' ## If it's not correct, this clears the first name variable for next iteration
        last_name = '' ## If it's not correct, this clears the last name variable for next iteration
        year_born = '' ## If it's not correct, this clears the year born variable for next iteration
        continue ## If the user says it's not correct it will go back to the top of the loop and ask them again


#Processing section

for employee in all_employee_data_in_tuples_list:
    employee_first_name = employee[0] ## This will take employee's first name out of the employee tuple and stick it into a variable called employee first name
    employee_last_name = employee[1] ## This will take employee's last name out of the employee tuple and stick it into a variable called employee last name
    employee_year_born = employee[2] ## This will take employee's year born out of the employee tuple and stick it into a variable called employee year born
    
    ## This is the employee data information that will be used to create employee usernames
    first_inital = employee_first_name[0].lower() ## Sets first inital as a variable that will take the first initial of an employee's first name and makes it lowercase format 
    last_name_username = employee_last_name.lower() ## Sets last name username as a varibale that will take an employee's last name and make it lowercase format
    last_two_digits_year_born = employee_year_born[-2:] ## Sets last two digits year born as a variable that will take the last two digits from an employee's year born 

    username = first_inital+last_name_username+last_two_digits_year_born ## Creates employee username by concatenating the information from the steps above (lines 81,82,83)

    if username in username_list: ## Test to see if the username is already in the username list 
        username = employee_first_name.lower() + employee_last_name[0:1].lower() + last_two_digits_year_born ## If the username is already in there then it will crete a new username a different way using the whole first name, first letter of the last name, and the last two digits of the year they were born
        username_list.append(username) ## This will then add the username to the username list
    else:
        username_list.append(username) ## This will add the username if it's not already in the list
    
    employee_data_dictionary[username] = employee ## This grabs employee data dictionary and puts in a key value equal to the username and pairs it to the employee tuple 
 


username_sorted_list = list(username_list) ## This makes a copy of username list 

username_sorted_list.sort() ## This sorts the list 

#Output section

print(date.today()) ## This displays the user's username
print(getpass.getuser()) ## This displays today's date 

print(all_employee_data_in_tuples_list) ## This displays the whole employee data list as the list is being built everytime a tuple is added
print(username_list) ## This will display the list of usernames after the program finishes going through the loop 
print(employee_data_dictionary) ## This displays the employee data dictionary 
print(username_sorted_list) ## This displays a sorted username list

for employee in all_employee_data_in_tuples_list:  
    employee_data_displayed = employee[0] + " " + employee[1] + " was born in " + employee[2] ## This sets the variable employee data displayed as a concatenation of the employee first name, last name, the words "was born in", and their year of birth all together 
    print(employee_data_displayed) ## This displays the concatenated sentence formed above in line 112 using the employee data the user entered (to form first name + last name + was born in + year born)
