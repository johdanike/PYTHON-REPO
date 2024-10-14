from os import remove


class Stack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = [] * capacity
        self.number = 0
        self.is_empty = True

    def stack_is_empty(self):
        self.is_empty = True

    def stack_is_not_empty(self):
        self.is_empty = False

    def get_is_empty(self):
        return self.is_empty

    # def push(self, param):
    #     # self.is_empty = False
    #     self.data.append(param)
    #     self.size += 1

    def push(self, param):
        if self.is_full():
            raise ValueError("Stack is full")
        self.data[self.number] = param
        self.number += 1

    def pop(self):
        for i in range(len(self.data)):
            remove(str(self.data[i-1]))
        return self.data



    def is_full(self):
        return self.number == self.capacity



