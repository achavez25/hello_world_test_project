#Import section

from datetime import date ## This imports the data library 
import getpass ## This imports getpass for username

#Flower Box section

###########################################################################
#
#   Name: Araceli Chavez
#   Date: 08/30/2022
#   Program Description: This program called username generator will use 
#   an employee's first name, last name, and year born to create usernames 
#   for them. It will display a employee data tuple list, full of tuples, a 
#   complete set of employee's usernames with duplicates, without dupliactes, 
#   a complete set of employee's usernames without duplicates converted to 
#   a list, and a sorted username list.
#
###########################################################################

#Variables section

username_list = [] ## This declares username list as a variable
username_sorted_list = [] ## This declares username sorted list as a variable 
employee_data_dictionary = {} ## This declares employee data dictionary as a variable 

#Input section

first_name_list = ['Araceli', 'Ana', 'Jimin', 'Yoongi', 'Taehyung'] ## Puts first name list data into a tuple
last_name_list = ['Chavez', 'Chavez', 'Park', 'Min', 'Kim'] ## Puts last name list data into a tuple
year_born_list = ['1995', '1995', '1990', '1985', '2000'] ## Puts year born list data into a tuple 

#Processing section 

all_employee_data_tuple = zip(first_name_list, last_name_list, year_born_list) ## Creates a all employee data tuple and zips it up
all_employee_data_tuple_list = list(all_employee_data_tuple) ## Creates a list from the all employee data tuple

for employee in all_employee_data_tuple_list:
    employee_first_name = employee[0] ## This will take employee's first name out of the employee tuple and stick it into a variable called employee first name
    employee_last_name = employee[1] ## This will take employee's last name out of the employee tuple and stick it into a variable called employee last name
    employee_year_born = employee[2] ## This will take employee's year born out of the employee tuple and stick it into a variable called employee year born
    
    ## This is the employee data information that will be used to create employee usernames
    first_inital = employee_first_name[0].lower() ## Sets first inital as a variable that will take the first initial of an employee's first name and makes it lowercase format 
    last_name_username = employee_last_name.lower() ## Sets last name username as a varibale that will take an employee's last name and make it lowercase format
    last_two_digits_year_born = employee_year_born[-2:] ## Sets last two digits year born as a variable that will take the last two digits from an employee's year born 

    username = first_inital+last_name_username+last_two_digits_year_born ## Creates employee username by concatenating the information from the steps above (lines 44,45,46)

    username_list.append(username) ## Adds created username to username list

    employee_data_dictionary[username] = employee ## Grabs employee data dictionary and puts in a key value equal to the username and pairs it to the employee tuple 

user_test_set = set(username_list) ## This converts the username list into a set called user test set

username_no_dups_list = list(user_test_set) ## This converts user test set from a set back to a list

for username in username_no_dups_list:
    username_sorted_list.append(username) ## This loops through the username no dups list and creates a second list called username sorted list 

username_sorted_list.sort() ## This sorts the username list 

#Output section

print(date.today()) ## This displays the user's username
print(getpass.getuser()) ## This displays today's date 

for emp_tuple in all_employee_data_tuple:
    print(emp_tuple) ## This displays tuples 

print(all_employee_data_tuple_list) ## This displays a list full of tuples called all employee data tuple list 
print(username_list) ## This displays a complete set of usernames including duplicates 
print(user_test_set) ## This displays a complete set of usernames without duplicates  
print(username_no_dups_list) ## This displays the user test set converted to a list 
print(username_sorted_list) ## This displays a sorted username list 