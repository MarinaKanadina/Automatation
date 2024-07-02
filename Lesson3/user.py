


class User:

       
    def __init__(self, _first_name, _last_name):
        self.first_name = _first_name
        self.last_name = _last_name

    def sayName(self):
        print(self.first_name)
        print(self.last_name)
        print(self.first_name, self.last_name)

        User = "my_user"

newUser = User ("Alina", "Канадина")

newUser.sayName()

