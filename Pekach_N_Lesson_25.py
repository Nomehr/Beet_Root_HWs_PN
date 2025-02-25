# Lesson 25
## Task 1

class UnsortedList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def index(self, item):
        if item in self.items:
            return self.items.index(item)
        else:
            raise ValueError(f"Item {item} not found in the list")

    def pop(self):
        if not self.items:
            raise IndexError("pop from empty list")
        return self.items.pop()

    def insert(self, index, item):
        self.items.insert(index, item)

    def slice(self, start, stop):
        return self.items[start:stop]

ulist = UnsortedList()
ulist.append(10)
ulist.append(20)
ulist.append(30)

print(ulist.items)

ulist.insert(1, 15)
print(ulist.items)

print(ulist.index(20))  # 2

ulist.pop()
print(ulist.items)

print(ulist.slice(0, 2))

## Task 2

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise IndexError("pop from empty stack")
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def peek(self):
        if self.top is None:
            raise IndexError("peek from empty stack")
        return self.top.data

    def is_empty(self):
        return self.top is None

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())
print(stack.peek())
print(stack.is_empty())
print(stack.pop())
print(stack.pop())
print(stack.is_empty())

## Task 3

class Queue:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = self.Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            raise IndexError("dequeue from empty queue")
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    def peek(self):
        if self.front is None:
            raise IndexError("peek from empty queue")
        return self.front.data

    def is_empty(self):
        return self.front is None

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())
print(queue.peek())
print(queue.is_empty())
print(queue.dequeue())
print(queue.dequeue())
print(queue.is_empty())