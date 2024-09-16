from User_profile import Users


class Admin(Users):
    def __init__(self, first_name, middle_name, last_name, age, phone_number, country, email, privileges):
        super().__init__(first_name, middle_name, last_name, age, phone_number, country, email)
        self.privileges = privileges

    def admin_privileges(self):
        privileges = ", ".join(self.privileges)
        print("The admin has the following privileges: " + privileges)



administrator = Admin("Kunda", "Santiago", "Ng'ambi", 19, 770714810, "Zambia",
                      "kundasantiagongambi@gmail.com", ["can add post", "can delete post", "can ban user"])
administrator.admin_privileges()