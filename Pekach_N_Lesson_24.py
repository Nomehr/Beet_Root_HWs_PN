# Lesson 24
## Task 1

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")

    def is_empty(self):
        return len(self.stack) == 0


def reverse_string(input_string: str) -> str:
    stack = Stack()
    for char in input_string:
        stack.push(char)

    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str


input_string = "Hello, World!"
print(reverse_string(input_string))

## Task 2

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")

    def is_empty(self):
        return len(self.stack) == 0


def is_balanced(expression: str) -> bool:
    stack = Stack()
    matching_brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in matching_brackets.values():
            stack.push(char)
        elif char in matching_brackets.keys():
            if stack.is_empty() or stack.pop() != matching_brackets[char]:
                return False
    return stack.is_empty()


expression = "{[()()]}"
print(is_balanced(expression))

expression = "{[(])}"
print(is_balanced(expression))

## Task 3

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")

    def is_empty(self):
        return len(self.stack) == 0

    def get_from_stack(self, item):
        if item in self.stack:
            self.stack.remove(item)
            return item
        else:
            raise ValueError(f"Element {item} not found in stack")


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def get_from_queue(self, item):
        if item in self.queue:
            self.queue.remove(item)
            return item
        else:
            raise ValueError(f"Element {item} not found in queue")


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

try:
    print(stack.get_from_stack(2))
    print(stack.get_from_stack(4))
except ValueError as e:
    print(e)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

try:
    print(queue.get_from_queue(2))
    print(queue.get_from_queue(4))
except ValueError as e:
    print(e)
