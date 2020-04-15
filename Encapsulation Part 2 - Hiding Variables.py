class User(object):

    def __init__(self, fName, lName, email, role):
        self.first_name = fName
        self.last_name = lName
        self.email = email
        self.__role = role

    def is_admin(self):
        if self.__role == 'admin':
            return True
        else:
            return False

    def __str__(self):
        out_str = 'Personal Name: ' + self.first_name + ' ' + self.last_name + '\n' + 'Email: ' + self.email + '\n' + 'Account Type: ' + self.role
        return out_str


first_name = 'Edward'
last_name = 'Yin'
email = 'edward@email.com'
role = 'admin'

user_1 = User(first_name, last_name, email, role)
print(user_1.is_admin())
