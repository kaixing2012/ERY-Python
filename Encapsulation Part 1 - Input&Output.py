class User(object):

    def __init__(self, fName, lName, email):
        first_name = fName
        last_name = lName
        email = email

    def __str__(self):
        out_str = 'Personal Name: ' + self.first_name + ' ' + self.last_name + '\n' + 'Email: ' + self.email + '\n'
        return out_str


first_name = 'Edward'
last_name = 'Yin'
email = 'edward@email.com'

user_1 = User(first_name, last_name, email)
pirnt(user_1)
