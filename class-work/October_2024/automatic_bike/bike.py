class Bike:
    def __init__(self):
        self._speed = 0
        self.__is_on = False
        self._gear = 0

    def get_is_on(self):
        return self.__is_on

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False

    def set_gear(self, speed):
        if 0 < speed <= 20:
            return 1
        elif 20 < speed <= 30:
            return 2
        elif 30 < speed <= 40:
            return 3
        elif speed > 40:
            return 4
        else: return 0

    def get_acceleration(self):
        if self.__is_on:
            speed_up = self.get_speed_increment()
            self._speed += speed_up
            self._gear = self.set_gear(self._speed)

    def get_speed_increment(self):
        return self._gear

    def set_speed_dec(self, speed):
        if self.get_is_on():
            speed_down = self.get_speed_decrement()
            self._speed -= speed_down
            self._gear = self.set_gear(self._speed)

    def get_speed_decrement(self):
        return self._gear

    def get_current_speed(self):
        return self._speed

    def get_current_gear(self):
        return self._gear


