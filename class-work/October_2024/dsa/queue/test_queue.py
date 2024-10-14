import unittest
from dsa.queue.queue import Queue

class TestQueue(unittest.TestCase):
    def test_that_i_enqueue_X_queue_is_not_empty(self):
        queue_test = Queue(4)
        given = queue_test.is_queue_empty()
        self.assertTrue(given)
        when = queue_test.enqueue("Software engineering")
        self.assertTrue(when)
        self.assertFalse(queue_test.is_queue_empty())

    def test_that_i_enqueueX_enqueue_Y_queue_is_not_empty(self):
        queue_test = Queue(4)
        given = queue_test.is_queue_empty()
        self.assertTrue(given)
        queue_test.enqueue("C##")
        queue_test.enqueue("Java")
        self.assertFalse(queue_test.is_queue_empty())

    def test_that_i_enqueueX_enqueueY_dequeue_Y_queue_is_not_empty(self):
        queue_test = Queue(4)
        given = queue_test.is_queue_empty()
        self.assertTrue(given)
        queue_test.enqueue("Software engineering")
        queue_test.enqueue("Java")
        queue_test.enqueue("C##")
        queue_test.enqueue("Python")
        self.assertFalse(queue_test.is_queue_empty())

    def test_that_i_enqueueX_enqueueY_dequeueX_queue_is_not_empty(self):
        queue_test = Queue(4)
        given = queue_test.is_queue_empty()
        self.assertTrue(given)
        queue_test.enqueue("Software engineering")
        queue_test.enqueue("Java")
        queue_test.dequeue()
        self.assertFalse(queue_test.is_queue_empty())

    def test_that_i_can_enqueue_X_enqueue_Y_elements_is_2_dequeue_x_i_have_1_element_left_queue_is_not_empty(self):
        queue_test = Queue(4)
        given = queue_test.is_queue_empty()
        self.assertTrue(given)
        queue_test.enqueue("Software engineering")
        queue_test.enqueue("Java")
        num_elements = queue_test.number_of_elements()
        self.assertEqual(num_elements, 2)
        queue_test.dequeue()
        self.assertFalse(queue_test.is_queue_empty())
        num_elements = queue_test.number_of_elements()
        self.assertEqual(num_elements, 1)

    def test_that_i_can_enqueue_X_dequeue_X_queue_is_now_empty(self):
        queue_test = Queue(4)
        given = queue_test.is_queue_empty()
        self.assertTrue(given)
        queue_test.enqueue("Software engineering")
        num_elements = queue_test.number_of_elements()
        self.assertEqual(num_elements, 1)
        queue_test.dequeue()
        self.assertTrue(queue_test.is_queue_empty())
        num_elements = queue_test.number_of_elements()
        self.assertEqual(num_elements, 0)



