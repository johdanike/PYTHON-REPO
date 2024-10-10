class AirConditioner:
    def __init__(self):
        self.__is_on = False
        self.temperature = 0

    def get_is_on(self):
        return self.__is_on

    def ac_is_on(self):
        self.__is_on = True

    def ac_is_off(self):
        self.__is_on = False

    def set_temperature(self, temperature):
        if self.get_is_on():
            if self.temperature < 16:
                self.temperature = 16
            elif self.temperature > 16:
                self.temperature = 30

    def get_temperature(self):
        return self.temperature

    def ac_can_increase_temperature(self):
        if self.get_is_on():
            if self.button_up():
                self.temperature +=1
            elif self.button_down():
                self.temperature -=1

    def button_up(self):
        pass

    def button_down(self):
        pass


