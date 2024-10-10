import unittest
from ac.ac import AirConditioner


class TestACFunctionalities(unittest.TestCase):
    def setUp(self):
        ac = AirConditioner()

    def test_i_have_an_ac_it_is_off_i_turn_it_on_it_is_on(self):
        ac = AirConditioner()
        given = ac.get_is_on()
        self.assertEqual(given, False)
        ac.turn_ac_on()
        when = ac.get_is_on()
        self.assertEqual(when, True)

    def test_that_i_have_an_ac_it_is_on_i_turn_it_off_it_is_off(self):
        ac = AirConditioner()
        ac.turn_ac_on()
        given = ac.get_is_on()
        self.assertEqual(given, True)
        ac.turn_ac_off()
        when = ac.get_is_on()
        self.assertEqual(when, False)

    def test_that_i_have_an_ac_it_is_on_and_in_16_i_increase_temp_it_increases(self):
        ac = AirConditioner()
        ac.turn_ac_on()
        given = ac.get_is_on()
        self.assertEqual(given, True)
        temp = ac.get_temperature()
        self.assertEqual(temp, 16)
        ac.increase_temp()
        new_temp = ac.get_temperature()
        self.assertEqual(new_temp, 17)

    def test_that_i_have_an_ac_it_is_on_i_and_temp_in_30_i_increase_temp_above_30_it_is_still_30(self):
        ac = AirConditioner()
        ac.turn_ac_on()
        given = ac.get_is_on()
        self.assertEqual(given, True)
        temp = ac.get_temperature()
        self.assertEqual(temp, 16)
        ac.set_temperature(30)
        new_temp = ac.get_temperature()
        self.assertEqual(new_temp, 30)
        ac.increase_temp()
        new_temp2 = ac.get_temperature()
        self.assertEqual(new_temp2, 30)
        ac.increase_temp()
        new_temp3 = ac.get_temperature()
        self.assertEqual(new_temp3, 30)

    def test_that_i_have_an_ac_it_is_on_i_decrease_temp_below_16_it_is_still_16(self):
        ac = AirConditioner()
        ac.turn_ac_on()
        given = ac.get_is_on()
        self.assertEqual(given, True)
        temp = ac.get_temperature()
        self.assertEqual(temp, 16)
        ac.decrease_temp()
        new_temp = ac.get_temperature()
        self.assertEqual(new_temp, 16)
        ac.decrease_temp()
        new_temp2 = ac.get_temperature()
        self.assertEqual(new_temp2, 16)

    def test_that_i_have_an_ac_it_is_on_temp_is_at_20_twice_i_decrease_temp_it_is_now_18(self):
        ac = AirConditioner()
        ac.turn_ac_on()
        given = ac.get_is_on()
        self.assertEqual(given, True)
        ac.set_temperature(20)
        temp = ac.get_temperature()
        self.assertEqual(temp, 20)
        ac.decrease_temp()
        new_temp = ac.get_temperature()
        self.assertEqual(new_temp, 19)
        ac.decrease_temp()
        new_temp2 = ac.get_temperature()
        self.assertEqual(new_temp2, 18)

    def test_that_i_have_an_ac_it_is_on_temp_is_at_20_i_decrease_temp_once_and_increase_it_is_now_20(self):
        ac = AirConditioner()
        ac.turn_ac_on()
        given = ac.get_is_on()
        self.assertEqual(given, True)
        ac.set_temperature(20)
        temp = ac.get_temperature()
        self.assertEqual(temp, 20)
        ac.decrease_temp()
        new_temp = ac.get_temperature()
        self.assertEqual(new_temp, 19)
        ac.increase_temp()
        new_temp2 = ac.get_temperature()
        self.assertEqual(new_temp2, 20)

    def test_that_ac_can_swing(self):
        ac = AirConditioner()
        ac.turn_ac_on()
        given = ac.get_is_on()
        self.assertEqual(given, True)
        ac.turn_swing_on()
        swing_state = ac.get_swing_mode()
        self.assertEqual(swing_state, True)

    def test_that_ac_swing_mode_can_be_paused(self):
        ac = AirConditioner()
        ac.turn_ac_on()
        given = ac.get_is_on()
        self.assertEqual(given, True)
        ac.turn_swing_off()
        swing_state = ac.get_swing_mode()
        self.assertEqual(swing_state, False)

    def test_that_ac_swing_mode_can_be_paused_and_unpaused(self):
        ac = AirConditioner()
        ac.turn_ac_on()
        given = ac.get_is_on()
        self.assertEqual(given, True)
        ac.turn_swing_on()
        swing_state = ac.get_swing_mode()
        self.assertEqual(swing_state, True)
        ac.turn_swing_off()
        swing_state = ac.get_swing_mode()
        self.assertEqual(swing_state, False)
        ac.turn_swing_on()
        swing_state = ac.get_swing_mode()
        self.assertEqual(swing_state, True)

    def test_that_ac_cannot_swing_when_ac_is_off(self):
        ac = AirConditioner()
        ac.turn_ac_off()
        given = ac.get_is_on()
        self.assertEqual(given, False)
        ac.turn_swing_on()
        swing_state = ac.get_swing_mode()
        self.assertRaises(ValueError, ac.turn_swing_off, True)


