import os
import json

DATABASE = 'contacts.json'

def load_contacts():
    """Load contacts from JSON database"""
    if not os.path.exists(DATABASE):
        return []
    with open(DATABASE, 'r') as file:
        return json.load(file)


def save_contacts(contacts):
    """save contacts from JSON database"""
    with open(DATABASE, 'w') as file:
        json.dump(contacts, file, indent=4)


def menu():
    """Show options list"""
    while True:
        print('1 to create a new contact')
        print('2 to show all contacts')
        print('3 to search')
        print('4 to update contact')
        print('5 to delete contact')
        print('6 to exit')
        menu_input = int(input('\nPlease, choose what you wont: '))

        if menu_input == 1:
            create_new_contact()
        elif menu_input == 2:
            show_all_contacts()
        elif menu_input == 3:
            search()
        elif menu_input == 4:
            update_contact()
        elif menu_input == 5:
            delete_contact()
        elif menu_input == 6:
            print('\nGoodbye!')
            break
        else:
            print('\nIncorrect enter. Please, try again.')


def create_new_contact():
    """Create a new one contact"""

    name = input('Please, enter name: ')
    surname = input('Please, enter surname: ')
    number = int(input('Please, enter phone number: '))
    city = input('Please, enter city: ')
    state = input('Please, enter state: ')
    country = input('Please, enter county: ')

    new_contact = {
        "name": name,
        "surname": surname,
        "number": number,
        "city": city,
        "state": state,
        "country": country
    }

    contacts = load_contacts()
    contacts.append(new_contact)
    save_contacts(contacts)

    print('\nContact created')


def show_all_contacts():
    """Show all contacts"""
    contacts = load_contacts()
    if not contacts:
        print('\nPhonebook is empty\n')
    else:
        print('\nContacts')
        for contact in contacts:
            if isinstance(contact, dict) and all(key in contact for key in ["name", "surname", "number", "city", "state", "country"]):
                print(
                    f'Name: {contact["name"]}, Surname: {contact["surname"]}\n,'
                    f'Tel.: {contact["number"]}, City: {contact["city"]}\n, '
                    f'Region: {contact["state"]}, Country: {contact["country"]}\n'
                )
            else:
                print(f'Error: {contact}')


def search():
    """Search contacts by keyword"""
    contacts = load_contacts()
    if not contacts:
        print('\nPhonebook is empty\n')
    key_word = input('Enter keyword to search: ')
    results = [contact for contact in contacts if key_word.lower() in json.dumps(contact).lower()]

    if results:
        print('\nSearch results: ')
        for contact in results:
            print(
                f'Name: {contact["name"]}, Surname: {contact["surname"]},'
                f'Tel.: {contact["number"]}, City: {contact["city"]}, '
                f'Region: {contact["state"]}, Country: {contact["country"]}\n'
            )
        else:
            print('\nNot found\n')

def update_contact():
    """Update contacts data"""

    search_key = input('Enter name, surname, tel, city, state or country to search & update')
    contacts = load_contacts()
    if not contacts:
        print('\nPhonebook is empty\n')
        return

    updated = False
    for contact in contacts:
        if search_key.lower() in json.dumps(contact).lower():
            print(f'Founded contacts info: {contact}')
            contact["name"] = input('New name: ') or contact["name"]
            contact["surname"] = input('New surname: ') or contact["surname"]
            contact["number"] = input('New number: ') or contact["number"]
            contact["city"] = input('New city: ') or contact["city"]
            contact["state"] = input('New state: ') or contact["state"]
            contact["country"] = input('New country: ') or contact["country"]
            updated = True

        if updated:
            save_contacts(contacts)
            print('\nContact updated\n')
        else:
            print('\nNot found\n')


def delete_contact():
    """Delete contact"""
    contacts = load_contacts()
    if not contacts:
        print('\nPhonebook is empty\n')
        return

    print('\nEnter name, surname, tel, city, state or country to search & delete: ')
    search_del = input('Enter: ')
    new_contacts = [contact for contact in contacts if search_del.lower() not in json.dumps(contact).lower()]

    if len(new_contacts) < len(contacts):
        save_contacts(new_contacts)
        print('\nContact deleted\n')
    else:
        print('\nNot found\n')


if __name__ == "__main__":
    menu()