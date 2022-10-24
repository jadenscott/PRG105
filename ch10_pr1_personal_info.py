"""
This program uses a class that holds personal information such as name, address, age and phone number. The personal
information will be printed to the console.
"""


class Contact:

    # initializes member variables
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    # getter and setter functions are defined for each variable
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_phone(self, phone):
        self.__phone = phone

    def get_phone(self):
        return self.__phone


def main():
    # objects are created out of the Contact class
    my_info = Contact('Jaden', 'Huntley, IL', 19, '111-312-2695')
    ago_info = Contact('Santiago', 'Normal, IL', 19, '222-345-1020')
    sis_info = Contact('Serena', 'Huntley, Il', 17, '847-284-1419')

    # getter functions are used to obtain the arguments passed
    print(f'{my_info.get_name()}, age {my_info.get_age()}\n{my_info.get_address()}\n{my_info.get_phone()}\n')
    print(f'{ago_info.get_name()}, age {ago_info.get_age()}\n{ago_info.get_address()}\n{ago_info.get_phone()}\n')
    print(f'{sis_info.get_name()}, age {sis_info.get_age()}\n{sis_info.get_address()}\n{sis_info.get_phone()}')


if __name__ == '__main__':
    main()
