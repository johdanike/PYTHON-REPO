import unittest

from automatic_bike.automatic_bike import AutomaticBike


class AutomaticBikeTest(unittest.TestCase):

    def test_that_bike_is_off(self):
      bike = AutomaticBike()
      when = bike.get_is_on()
      bike.turn_bike_off()
      self.assertFalse(when)

    def test_bike_is_on_i_turn_it_off_it_is_off(self):
        bike = AutomaticBike()
        bike.turn_bike_on()
        bike_is_on = bike.get_is_on()
        self.assertTrue(bike_is_on)
        bike.turn_bike_off()
        bike_is_off = bike.get_is_on()
        self.assertFalse(bike_is_off)

    def test_bike_is_on_and_on_gear1_i_accel_speed_is_15(self):
        bike = AutomaticBike()
        bike.turn_bike_on()
        current_state =bike.get_is_on()
        self.assertTrue(current_state)
        for index in range(15):
            bike.set_acceleration()
        current_speed = bike.get_speed()
        self.assertEqual(15, current_speed)

    def test_bike_is_on_and_on_gear1_i_accel_speed_is_15_i_accel_again_speed_is_16(self):
        bike = AutomaticBike()
        bike.turn_bike_on()
        current_state = bike.get_is_on()
        self.assertTrue(current_state)
        for index in range(15):
            bike.set_acceleration()
        current_speed = bike.get_speed()
        self.assertEqual(15, current_speed)
        bike.set_acceleration()
        current_speed = bike.get_speed()
        self.assertEqual(16, current_speed)

    def test_bike_is_on_and_on_gear2_current_speed_is_24_i_accel_speed_is_26(self):
        bike = AutomaticBike()
        bike.turn_bike_on()
        current_state = bike.get_is_on()
        self.assertTrue(current_state)
        for index in range(24):
            bike.set_acceleration()
        current_speed = bike.get_speed()-1
        self.assertEqual(26, current_speed)
        # bike.set_acceleration()
        # self.assertEqual(26, current_speed)

    def test_that_bike_is_on_and_on_gear_3_current_speed_is_31_i_accel_it_becoes_34(self):
        bike = AutomaticBike()
        bike.turn_bike_on()
        current_state = bike.get_is_on()
        self.assertTrue(current_state)
        for index in range(31):
            bike.set_acceleration()
        current_speed = bike.get_speed()
        self.assertEqual(34, current_speed)

