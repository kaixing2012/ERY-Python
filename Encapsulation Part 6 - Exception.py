import re


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

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, newName):
        p = re.compile(r'(\W|\d)')
        m = p.findall(newName)

        if not m:
            self.__first_name = newName
            print('the value is changed')
        else:
            raise ValueError('given value can only be langauge charactor')

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, newName):
        p = re.compile(r'(\W|\d)')
        m = p.findall(newName)

        if not m:
            self.__last_name = newName
            return True
        else:
            return False

    @property
    def personal_name(self):
        return self.first_name + ' ' + self.last_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, newEmail):
        p = re.compile(r'[a-zA-Z0-9_.]+\@[a-zA-Z]+\.[a-zA-Z]+')
        m = p.findall(newEmail)

        if m:
            self.__email = newEmail
            return True
        else:
            return False

    @property
    def role(self):
        if self.__role is not None:
            return self.__role
        else:
            return 'There is no value'

    @role.setter
    def role(self, newRole):
        roles = ['member', 'admin']

        if newRole in roles:
            self.__role = newRole
            return True
        else:
            return False

    @property
    def is_admin(self):
        if self.__role == 'admin':
            return True
        else:
            return False

    def __str__(self):
        out_str = 'Personal Name: ' + self.__first_name + ' ' + self.__last_name + '\n' + 'Email: ' + self.__email + '\n' + 'Account Type: ' + str(self.__role)
        return out_str


first_name = 'Edward'
last_name = 'Yin'
email = 'edward@email.com'
role = 'admin'

user_1 = User(first_name, last_name, email)

try:
    user_1.first_name = 'A'

except ValueError as v:
    print(v)
