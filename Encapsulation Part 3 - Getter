class User(object):
    __first_name = ''
    __last_name = ''
    __email = ''
    __role = ''

    def __init__(self, fName, lName, email, role=None):
        self.__first_name = fName
        self.__last_name = lName
        self.__email = email
        self.__role = role

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_personal_name(self):
        return self.get_first_name() + ' ' + self.get_last_name()

    def get_role(self):
        if self.__role is not None:
            return self.__role
        else:
            return 'There is no value'

    def is_admin(self):
        if self.__role == 'admin':
            return True
        else:
            return False

    def __str__(self):
        out_str = 'Personal Name: ' + self.__first_name + ' ' + self.__last_name + '\n' + 'Email: ' + self.__email + '\n' + 'Account Type: ' + self.__role
        return out_str


first_name = 'Edward'
last_name = 'Yin'
email = 'edward@email.com'
role = 'admin'

user_1 = User(first_name, last_name, email)
print(user_1.get_role())
print(user_1.get_personal_name())
print(user_1.get_first_name())
