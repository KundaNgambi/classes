class Users:
    def __init__(self, first_name, middle_name, last_name, age, country_code, phone_number, email):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.email = email
        self.country_code = country_code

    def users_name(self):
        if self.middle_name.title() == "None":
            print("Name: " + self.first_name + " " + self.last_name)
        elif self.middle_name.title() != "None":
            print("Name: " + self.first_name + " " + self.middle_name + " " + self.last_name)
        else:
            print("If user has no middle name, enter middle name as None.")

    def users_age(self):
        print("Age: " + self.age + " years")

    def users_phone_number(self):
        print("Phone Number: " + self.country_code + self.phone_number)

    def users_email(self):
        print("Email: " + self.email)


#user_input
user_first_name = input("Enter first name: ")
user_middle_name = input("Enter middle name(Enter None if none given): ")
user_last_name = input("Enter last name: ")
user_age = input("Enter your age: ")
user_country_code = input("Enter your country code: ")
user_phone_number = input("Enter your phone_number: ")
user_email = input("Enter your email: ")
print()

#intantiate
my_details = Users(user_first_name, user_middle_name, user_last_name, user_age, user_country_code, user_phone_number,
                   user_email)
my_details.users_name()
my_details.users_age()
my_details.users_phone_number()
my_details.users_email()
