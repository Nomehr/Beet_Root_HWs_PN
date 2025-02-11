# Lesson 16
## Task 1

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        return f'Hi! My name is {self.name}, i\'m {self.age} years old.'


class Student(Person):
    def __init__(self, name, age, target, deadline):
        super().__init__(name, age)
        self.target = target
        self.deadline = deadline

    def talk1(self):
        return f'Hi! I\'am {self.name}! I need {self.target} before {self.deadline} come!'


class Teacher(Person):
    def __init__(self, name, age, job, work):
        super().__init__(name, age)
        self.job = job
        self.work = work

    def talk2(self):
        return f'Hello! My name is {self.name}. I am a {self.job} and I {self.work} here everyday!'


student = Student('John', 20, 'make some math', 'December')
teacher = Teacher('Boris', 40, 'Teacher', 'check students homeworks')

print(student.talk1())
print(teacher.talk2())

## Task 2

class Mathematician:
    def square_nums(self, nums):
        return [num ** 2 for num in nums]

    def remove_positives(self, nums):
        return [num for num in nums if num <= 0]

    def filter_leaps(self, years):
        return [year for year in years if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

## Task 3

class Product:
    def __init__(self, type_, name, price):
        self.type = type_
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = {}
        self.income = 0

    def add(self, product, amount):
        if amount <= 0:
            raise ValueError("Product amount must be greater than 0.")

        price_with_markup = product.price * 1.3

        if product.name in self.products:
            self.products[product.name]["amount"] += amount
        else:
            self.products[product.name] = {
                "price": price_with_markup,
                "amount": amount,
                "discount": 0
            }

    def set_discount(self, name, percent):
        if name not in self.products:
            raise ValueError(f"Product '{name}' not found.")

        if percent < 0 or percent > 100:
            raise ValueError("Discount must be between 0 and 100.")

        self.products[name]["discount"] = percent

    def sell_product(self, name, amount):
        if name not in self.products:
            raise ValueError(f"Product '{name}' is out of stock.")

        if self.products[name]["amount"] < amount:
            raise ValueError("Not enough stock available.")

        discount = self.products[name]["discount"] / 100
        final_price = self.products[name]["price"] * (1 - discount)

        self.income += final_price * amount
        self.products[name]["amount"] -= amount

        if self.products[name]["amount"] == 0:
            del self.products[name]

    def get_income(self):
        return self.income

    def get_product_info(self, name):
        if name not in self.products:
            raise ValueError(f"Product '{name}' is out of stock.")
        return name, self.products[name]["amount"]


p1 = Product('Clothing', 'T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

store = ProductStore()
store.add(p1, 10)
store.add(p2, 300)

store.sell_product('Ramen', 10)

print(store.get_product_info('Ramen'))
print(store.get_income())

## Task 4

class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        with open("logs.txt", "a") as log_file:
            log_file.write(msg + "\n")


try:
    raise CustomException("Error!")
except CustomException as e:
    print(f"Error: {e}")