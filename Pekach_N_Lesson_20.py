#Lesson 20

import unittest
import json
import os

TEST_DATABASE = 'test_contacts.json'

def load_contacts(database=TEST_DATABASE):
    if not os.path.exists(database):
        return []
    with open(database, 'r') as file:
        return json.load(file)


def save_contacts(contacts, database=TEST_DATABASE):
    with open(database, 'w') as file:
        json.dump(contacts, file, indent=4)


class PhonebookTests(unittest.TestCase):
    def setUp(self):
        self.contacts = [
            {"name": "John", "surname": "Doe", "number": "1234567890", "city": "NYC", "state": "NY", "country": "USA"},
            {"name": "Jane", "surname": "Doe", "number": "0987654321", "city": "LA", "state": "CA", "country": "USA"}
        ]
        save_contacts(self.contacts, TEST_DATABASE)

    def tearDown(self):
        if os.path.exists(TEST_DATABASE):
            os.remove(TEST_DATABASE)

    def test_load_contacts(self):
        contacts = load_contacts(TEST_DATABASE)
        self.assertEqual(len(contacts), 2)

    def test_save_contacts(self):
        new_contact = {"name": "Alice", "surname": "Smith", "number": "1122334455", "city": "Boston", "state": "MA",
                       "country": "USA"}
        self.contacts.append(new_contact)
        save_contacts(self.contacts, TEST_DATABASE)
        contacts = load_contacts(TEST_DATABASE)
        self.assertEqual(len(contacts), 3)
        self.assertEqual(contacts[-1]["name"], "Alice")

    def test_search_contact(self):
        contacts = load_contacts(TEST_DATABASE)
        key_word = "Jane"
        results = []
        for contact in contacts:
            if key_word.lower() in json.dumps(contact).lower():
                results.append(contact)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Jane")


if __name__ == '__main__':
    unittest.main()