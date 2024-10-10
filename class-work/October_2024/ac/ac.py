class AirConditioner:
    def __init__(self):
        self.__is_on = False
        self.temperature = 16
        self.__swing = False

    def get_is_on(self):
        return self.__is_on

    def turn_ac_on(self):
        self.__is_on = True

    def turn_ac_off(self):
        self.__is_on = False

    def get_swing_mode(self):
        return self.__swing

    def turn_swing_on(self):
        if self.get_is_on():
            self.__swing = True
        else:
            raise ValueError("AC must be turned on")

    def turn_swing_off(self):
        if self.get_is_on():
            self.__swing = False
        else:
            raise ValueError("AC must be turned on")

    def set_temperature(self, temperature):
        if self.get_is_on():
            self.temperature = temperature
            if self.temperature <= 16:
                self.temperature = 16
            elif self.temperature >= 30:
                self.temperature = 30
            self.temperature = temperature

    def get_temperature(self):
        return self.temperature

    def increase_temp(self):
        if self.get_is_on():
            if self.get_temperature() >= 30:
                self.temperature = self.get_temperature()
            else: self.temperature += 1
        return self.temperature

    def decrease_temp(self):
        if self.get_is_on():
            if self.get_temperature() <= 16:
                self.temperature = self.get_temperature()
            else: self.temperature -= 1
        return self.temperature




