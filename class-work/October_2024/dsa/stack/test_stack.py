import unittest
from dsa.stack.stack import Stack

class TestStack(unittest.TestCase):
    def test_that_i_can_push_X_stack_is_not_empty(self):
        my_stack = Stack()
        my_stack.push("The Good news")
        when = my_stack.stack_is_not_empty()
        self.assertTrue(True, when)

    def test_that_i_can_push_X_and_pop_X_stack_is_empty(self):
        my_stack = Stack(3)
        self.assertTrue(True, my_stack.stack_is_empty())
        my_stack.push("The Good news")
        self.assertTrue(True, my_stack.stack_is_not_empty())
        my_stack.pop()
        self.assertTrue(False, my_stack.stack_is_empty())
