

class Stack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = [None] * capacity
        self.number = 0
        self.is_empty = True

    def stack_is_empty(self):
        self.is_empty = True

    def stack_is_not_empty(self):
        self.is_empty = False

    def get_is_empty(self):
        return self.is_empty

    def push(self, param):
        if self.is_full():
            raise ValueError("Stack is full")
        self.data[self.number] = param
        self.number += 1

    def pop(self):
        for index in range(len(self.data)):
            str(self.data[index-1])
            self.number -= 1
        return self.data

    def get_number(self):
        return self.number

    def is_full(self):
        return self.number == self.capacity



