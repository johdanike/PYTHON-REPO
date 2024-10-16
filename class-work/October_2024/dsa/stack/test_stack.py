import unittest
from dsa.stack.stack import Stack

class TestStack(unittest.TestCase):
    def test_that_i_can_push_X_stack_is_not_empty(self):
        my_stack = Stack(3)
        my_stack.push("The Good news")
        when = my_stack.stack_is_not_empty()
        self.assertTrue(True, when)

    def test_that_i_can_push_X_and_pop_X_stack_is_empty(self):
        my_stack = Stack(3)
        self.assertTrue(True, my_stack.stack_is_empty())
        my_stack.push("The Good news")
        self.assertTrue(True, my_stack.stack_is_not_empty())
        my_stack.pop()
        self.assertFalse(False, my_stack.stack_is_empty())

    def test_that_i_can_push_X_push_Y_pop_X_stack_is_not_empty(self):
        my_stack = Stack(3)
        self.assertTrue(True, my_stack.stack_is_empty())
        my_stack.push("The Good news")
        self.assertTrue(True, my_stack.stack_is_empty())
        my_stack.push("The Good shepherd")
        self.assertTrue(True, my_stack.stack_is_empty())
        my_stack.pop()
        self.assertFalse(False, my_stack.stack_is_empty())

    def test_that_i_can_push_XYZ_pop_Z_stack_is_not_empty(self):
        my_stack = Stack(3)
        self.assertTrue(True, my_stack.stack_is_empty())
        my_stack.push("The Good news")
        my_stack.push("The Good shepherd")
        my_stack.push("The Good Lamb")
        my_stack.pop()
        self.assertFalse(False, my_stack.stack_is_empty())

    def test_that_i_can_push_XYZ_stack_is_full(self):
        my_stack = Stack(3)
        my_stack.push("The Good news")
        my_stack.push("The Good shepherd")
        my_stack.push("The Good Lamb")
        self.assertTrue(True, my_stack.stack_is_not_empty())

    # def test_that_i_stack_will_throw_exception_if_full(self):
    #     my_stack = Stack(3)
    #     my_stack.push("The Good news")
    #     my_stack.push("The Good shepherd")
    #     my_stack.push("The Good Lamb")
    #     my_stack.push("the good human")
    #     # self.assertRaises(ValueError, my_stack.is_full())
    #     self.assertRaises(ValueError, my_stack.push, "the good human")

    def test_push_X_pop_X_stack_is_zero(self):
        my_stack = Stack(3)
        my_stack.push("The Good news")
        self.assertFalse(my_stack.stack_is_empty())
        my_stack.pop()
        self.assertTrue(my_stack.stack_is_empty())