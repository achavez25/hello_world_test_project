"""A set of classes that can be used to represent employees"""

from person import Person
import random

class Employee(Person):

    """Models asspects of a person specific to an employee"""

    ## This builds our class Employee when somebody calls to it 
    def __init__(self, first_name, last_name, birth_year, password_length, use_special_characters, use_numbers):
        super().__init__(first_name, last_name, birth_year)
        self.password_length = password_length
        self.use_special_characters = use_special_characters
        self.use_numbers = use_numbers

    ## This function uses constants and variables to go get values to build our password
    def build_password(self):
        ALPHABET = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        SPECIAL_CHARACTERS = "!@#$%^&*"
        NUMBERS = "0123456789"
        count = 0
        password = ""

        ## This loop will iterate until it reaches the password length the user entered so if the count is less than the password length the user entered it will go through all the characters in the function build password and grabs a character from the string ALPHABET using the randomNumber variable and updates the password variable with it then clears the pwChar and increments the count variables if this logic is followed  
        while count < self.password_length:
            randomNumber = random.randrange(0,51,1)
            pwChar = ALPHABET[randomNumber]
            password = password + pwChar
            pwChar = ""
            count = count + 1

            ## If the user asks for special characters and the count has not exceeded the length of the password this grabs a character from the string SPECIAL CHARACTERS using the randomNumber variable and updates the password variable with it then clears the pwChar and increments the count variables if this logic is followed  
            if self.use_special_characters and count < self.password_length:
                randomNumber = random.randrange(0,7,1)
                pwChar = SPECIAL_CHARACTERS[randomNumber]
                password = password + pwChar
                pwChar = ""
                count = count + 1

            ## If the user asks for numbers and the count has not exceeded the length of the password this grabs a character from the string NUMBERS using the randomNumber variable and updates the password variable with it then clears the pwChar and increments the count variables if this logic is followed  
            if self.use_numbers and count < self.password_length:
                randomNumber = random.randrange(0,9,1)
                pwChar = NUMBERS[randomNumber] 
                password = password + pwChar
                pwChar = ""
                count = count + 1

        return password ## This returns the password wherever it was called in our main program