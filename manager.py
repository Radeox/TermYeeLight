import sys
import time
import yeelight
from settings import IP


class SmartBulb:
    mode = {
        "default": {
            "color_temp": 3000,
            "brightness": 66,
        },
        "evening": {
            "color_temp": 1000,
            "brightness": 33,
        },
        "work": {
            "color_temp": 7000,
            "brightness": 100,
        },
    }

    def __init__(self, ip_address):
        self.bulb = yeelight.Bulb(ip_address)
        self.status = self.bulb.get_properties()['power']

    def set_power(self, power):
        if power == True:
            self.status = 'on'
            self.bulb.turn_on()
            print("Turning on.")
        else:
            self.status = 'off'
            self.bulb.turn_off()
            print("Turning off.")

    def toggle_power(self):
        if self.is_on:
            self.set_power(False)
        else:
            self.set_power(True)

    def set_mode(self, mode):
        if mode not in self.mode:
            print("Wrong mode!\nAvailable modes:")
            for mode in self.mode.keys():
                print(f"- {mode}")
        elif not self.is_off:
            self.set_power(True)

        color_temp = self.mode[mode]['color_temp']
        brightness = self.mode[mode]['brightness']
        self.bulb.set_color_temp(color_temp)
        self.bulb.set_brightness(brightness)
        print(f"Setting mode '{mode}'.")

    @property
    def is_on(self):
        return True if self.status == 'on' else False

    @property
    def is_off(self):
        return True if self.status == 'off' else False


if __name__ == "__main__":
    try:
        bulb = SmartBulb(IP)
    except yeelight.main.BulbException:
        print("Yeelight is unreachable!")
    else:
        if len(sys.argv) > 1:
            param = sys.argv[1]
            bulb.set_mode(param)
        else:
            bulb.toggle_power()
