import datetime

class Person:

    """Models aspects of a person"""
    
    ## This builds our class Person when somebody calls to it 
    def __init__(self, first_name, last_name, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    ## This returns a greeting message to show in our main program
    def greet_person(self):
        greeting = f"Welcome, {self.first_name}."  

        return greeting 
    
    ## This returns the age of the user to show in our main program
    def age(self):
        today = datetime.date.today()  
        age = today.year - int(self.birth_year)

        return age 