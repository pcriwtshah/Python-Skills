class Users():
    def __init__(self, first_name, last_name, date_of_birth, address, marital_status, job_status):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.marital_status = marital_status
        self.job_status = job_status

    def describe_user(self):
        print(self.first_name.title() + " is " + self.job_status + "\n")

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title()+"\n")

person_1 = Users('tom', 'smith', " ", " ", 'single', 'employed')
person_2 = Users('Harry', 'Gomez', "12/15/2000 ", " ", 'married', 'unemployed')
#print(person_1.first_name.title())

person_1.describe_user()
person_1.greet_user()
print("\n\n")
person_2.describe_user()
person_2.greet_user()
