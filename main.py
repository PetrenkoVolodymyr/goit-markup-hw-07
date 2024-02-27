from classes import AddressBook, Record

#DECORATORS
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name, phone and/or birthday please."
        except KeyError:
            return "Enter user name"
        except IndexError:
            return "Enter user name"
    return inner


#MAIN FUNCTIONS
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book:AddressBook):
    name, phone = args
    record = book.find(name)
    if not record:
        record = Record(name)
        book.add_record(record)
    record.add_phone(phone)
    return 'Contact added'

    
@input_error
def change_contact(args, book:AddressBook):
    name, phone_old, phone_new = args
    record = book.find(name)
    record.edit_phone(phone_old, phone_new)
    return 'Contact changed'


@input_error 
def show_all(args, book:AddressBook):
    return book


@input_error
def get_contact(args, book:AddressBook):
    name = args[0]
    record = book.find(name)
    return record.phone_list()

@input_error
def del_contact(args, book:AddressBook):
    name, phone = args
    record = book.find(name)
    record.remove_phone(phone)
    return 'Phone deleted'


@input_error
def get_birthday(args, book:AddressBook):
    name = args[0]
    record = book.find(name)
    return record.birthday


@input_error
def add_birthday(args, book:AddressBook):
    name, date = args
    record = book.find(name)
    if not record:
        record = Record(name)
        book.add_record(record)
    record.add_birth(date)
    return 'Birthday added'

@input_error
def to_congratulate(args, book:AddressBook):
    return book.get_upcoming_birthdays()



def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "all":
            print(show_all(args, book))
        elif command == "phone":
            print(get_contact(args, book))
        elif command == "delete":
            print(del_contact(args, book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(get_birthday(args, book))
        elif command == "birthdays":
            print(to_congratulate(args, book))


        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()