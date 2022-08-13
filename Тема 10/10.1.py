class MyException(Exception):
    def __init__(self, message):
        self.txt = message

def check_name(name):
    for i in name:
        if i.isdigit():
            raise MyException('Имя не может содержать в себе цифры')
    print(name)

check_name('Vova')
check_name('Vova213')