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

    def get_first_name(self):
        return self.__first_name

    # r'(\W|\d)'
    def set_first_name(self, newName):
        p = re.compile(r'(\W|\d)')
        m = p.findall(newName)

        if not m:
            self.__first_name = newName
            return True
        else:
            return False

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, newName):
        p = re.compile(r'(\W|\d)')
        m = p.findall(newName)

        if not m:
            self.__last_name = newName
            return True
        else:
            return False

    def get_personal_name(self):
        return self.get_first_name() + ' ' + self.get_last_name()

    def get_email(self):
        return self.__email

    # r'[a-zA-Z0-9_.]+\@[a-zA-Z]+\.[a-zA-Z]+'
    def set_email(self, newEmail):
        p = re.compile(r'[a-zA-Z0-9_.]+\@[a-zA-Z]+\.[a-zA-Z]+')
        m = p.findall(newEmail)

        if m:
            self.__email = newEmail
            return True
        else:
            return False

    def get_role(self):
        if self.__role is not None:
            return self.__role
        else:
            return 'There is no value'

    def set_role(self, newRole):
        roles = ['member', 'admin']

        if newRole in roles:
            self.__role = newRole
            return True
        else:
            return False

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
