# Lesson 15
## Task 1

class Person():

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f'Hello! My name is {self.firstname} {self.lastname} and i\'m {self.age} years old')

result = Person('Carl', 'Johnson', 26)
result.talk()

## Task 2

class Dog:

    age_factor = 7

    def __init__(self,dogage):
        self.dogage = dogage

    def human_age(self):
        return self.dogage * self.age_factor

result = Dog(5)
print(f'Dogs age in human equivalent equals to {result.human_age()}')

## Task 3

class TVController:

    def __init__(self, channels):
        self.channels = channels
        self.channel_index = 0

    def first_channel(self):
        self.channel_index = 0
        return self.channels[self.channel_index]

    def last_channel(self):
        self.channel_index = len(self.channels) - 1
        return self.channels[self.channel_index]

    def turn_channel(self, n):
        if 1 <= n <= len(self.channels):
            self.channel_index = n - 1
            return self.channels[self.channel_index]
        return 'No'

    def next_channel(self):
        self.channel_index = (self.channel_index + 1) % len(self.channels)
        return self.channels[self.channel_index]

    def previous_channel(self):
        self.channel_index = (self.channel_index - 1) % len(self.channels)
        return self.channels[self.channel_index]

    def current_channel(self):
        return self.channels[self.channel_index]

    def exists(self, param):
        if isinstance(param, int):
            return 'Yes' if 1 <= param <= len(self.channels) else 'No'
        elif isinstance(param, str):
            return 'Yes' if param in self.channels else 'No'
        return 'No'


CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.exists(4))
print(controller.exists("BBC"))