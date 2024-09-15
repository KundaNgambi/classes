import phonenumbers as pn
from phonenumbers import geocoder, carrier
import pycountry

class Users:
    def __init__(self, first_name, middle_name, last_name, age, phone_number, country, email):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.email = email
        self.country = country

    def users_name(self):
        if self.middle_name.title() == "None":
            print("Name: " + self.first_name + " " + self.last_name)
        elif self.middle_name.title() != "None":
            print("Name: " + self.first_name + " " + self.middle_name + " " + self.last_name)
        else:
            print("If user has no middle name, enter middle name as None.")

    def users_age(self):
        print("Age: " + self.age + " years")

    def users_country(self):
        print("Country: " + self.country.title())
    def users_phone_number(self):
        try:
            country_data = pycountry.countries.get(name=self.country)
            if country_data:
                country_code = pn.country_code_for_region(country_data.alpha_2)
                phone_number_obj = pn.parse(f"+{country_code}{self.phone_number}")
                formatted_number = pn.format_number(phone_number_obj, pn.PhoneNumberFormat.INTERNATIONAL)
                print("Phone Number: " + formatted_number)
            else:
                print("Invalid country name.")
        except Exception as e:
            print(f"Error processing phone number: {e}")

    def users_email(self):
        print("Email: " + self.email)

#user_input
user_first_name = input("Enter first name: ")
user_middle_name = input("Enter middle name(Enter None if none given): ")
user_last_name = input("Enter last name: ")
user_age = input("Enter your age: ")
user_country = input("Enter your country : ")
user_phone_number = input("Enter your phone_number: ")
user_email = input("Enter your email: ")
print()

#intantiate
my_details = Users(user_first_name, user_middle_name, user_last_name, user_age, user_phone_number, user_country, user_email)
my_details.users_name()
my_details.users_age()
my_details.users_phone_number()
my_details.users_email()
