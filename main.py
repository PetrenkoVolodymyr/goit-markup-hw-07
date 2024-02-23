from collections import UserDict
import datetime
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # реалізація класу
    pass
	

class Phone(Field):
    
    def __init__(self, value):
        if not self.check_phone(value):
            raise ValueError("Not 10 digits") 
        super().__init__(value)

    def check_phone(self, value):
        return len(value) == 10 and value.isdigit()
    

class Birthday(Field):
    def __init__(self, value):
        try:
            date = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(date)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, value):
        number=Phone(value) 
        if number.check_phone(value):
            self.phones.append(number)

    def __str__(self):
        try:
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday.value}"
        except:
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def get_phone(self):
        for p in self.phones:
            return(p)
        
    def add_birthday(self, birthday):
        date = Birthday(birthday) 
        self.birthday = date    
        return self.birthday   
    
    def getbirthday(self):
        return self.birthday.value
    
class AddressBook(UserDict):
    def add_record(self, name, phone):
        item = Record(name)
        item.add_phone(phone)
        self.data[name] = item

    def find(self, name):
        if self.data.get(name) is None:
            print("Name is not available.")
        else:
            print(self.data.get(name))
            
    def delete(self, name):
        try:
            del self.data[name]
        except:
            print(f'No name {name}')

    def getname(self, name):
        return self.data[name].get_phone()  
    
    # @input_error
    def add_birth(self, name, birthday):
        return self.data[name].add_birthday(birthday)
 
    # @input_error
    def show_birthday(self, name):
        return self.data[name].getbirthday()

    # @input_error
    def birthdays(self):
        birth_list=[]
        for i in self.data:
            birth_dict = {}
            birth_dict['name'] = i
            birth_dict['birthday'] = self.show_birthday(birth_dict["name"])
            birth_list.append(birth_dict)
        
        upcoming_birthdays=[]
        for user in birth_list:

            birthday = user["birthday"]
            today = datetime.today().date()
            curr_birthday = datetime(today.year, birthday.month, birthday.day).date()

            diff = curr_birthday - today

            if diff <= timedelta(days=6) and diff>= timedelta(days=0):
                if curr_birthday.weekday() == 5:
                    curr_birthday = curr_birthday + timedelta(days=2)
                if curr_birthday.weekday() == 6:
                    curr_birthday = curr_birthday + timedelta(days=1)

                cong_date_str = curr_birthday.strftime("%Y-%m-%d")

                to_congratulate = {"name": user["name"], "congratulation_date": cong_date_str}
                upcoming_birthdays.append(to_congratulate.copy())

        return upcoming_birthdays


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if len(args)==1:
            name=args[0]
        elif len(args)==2:
            name, secondinput = args

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            book.add_record(name, secondinput)
            print("Contact added.")


        elif command == "change":
            book.delete(name)
            book.add_record(name, secondinput)

        elif command == "phone":
            print(book.getname(name))
            

        elif command == "all":
            for i in list(book):
                book.find(i)

        elif command == "add-birthday":
            book.add_birth(name, secondinput)
            
        elif command == "show-birthday":
            print(book.show_birthday(name))

        elif command == "birthdays":
            print(book.birthdays())

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
   