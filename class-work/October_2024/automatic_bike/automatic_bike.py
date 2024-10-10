class AutomaticBike:

    def __init__(self):
        self.__is_on = False
        self.speed = 0
        self.gear = 1

    def turn_bike_on(self):
        self.__is_on = True
    def turn_bike_off(self):
        self.__is_on = False
    def get_is_on(self):
        return self.__is_on

    def set_acceleration(self):
        if self.get_is_on():
            if self.get_gear() == 1:
                self.speed += 1
            if self.get_gear() == 2:
                self.speed += 2
            if self.get_gear() == 3:
                self.speed += 3
            if self.get_gear() == 4:
                self.speed += 4
        self.set_gear()

    def get_speed(self):
        return self.speed

    def set_gear(self):
        if self.get_is_on():
            if 0 < self.get_speed() <= 20:
                self.gear = 1
            elif 20 < self.get_speed() <= 30:
                self.gear = 2
            elif 30 < self.get_speed() <= 40:
                self.gear = 3
            else:
                self.gear = 4

    def get_gear(self):
        return self.gear

    def set_deceleration(self):
        if self.get_is_on():
            if self.get_gear() == 1:
                self.speed -= 1
            elif self.get_gear() == 2:
                self.speed -= 2
            elif self.get_gear() == 3:
                self.speed -= 3
            elif self.get_gear() == 4:
                self.speed -= 4
            else:
                self.speed = 0