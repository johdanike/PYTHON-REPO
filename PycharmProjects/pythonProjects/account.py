class Account:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0.00
        self.account_number = 0
        self.pin = "0000"

    def  change_pin(self, old_pin , new_pin):
        if self.pin == old_pin and len(new_pin) == 4:
            self.pin = new_pin
        else:
            return "Invalid old pin"

        # message = self.pin = new_pin if self.pin == old_pin else "Invalid old pin"
        # return message


