class Nikola:
    def __init__(self, name, age):
        if name != 'Николай':
            self.name = f'Я не {name},а Николай'
        else:
            self.name = 'Николай'
        self.age = age

    def get_name(self):
        print(self.name)

new_name = Nikola('Михаил', 19)
new_name.get_name()

new_name = Nikola('Николай', 19)
new_name.get_name()

