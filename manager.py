import sys
import time
from yeelight import Bulb
from settings import IP

class SmartBulb:
    mode = {
        "work": {
            "color_temp": 7000,
        },
        "evening": {
            "color_temp": 1000,
        },
    }

    def __init__(self):
        self.bulb = Bulb(IP)
        self.status = self.bulb.get_properties()['power']

    def toggle_power(self):
        if self.status == 'on':
            self.status = 'off'
            self.bulb.turn_off()
            print("Turning off.")
        else:
            self.status = 'on'
            self.bulb.turn_on()
            print("Turning on.")
    
    def set_mode(self, mode):
        if self.status == 'off':
            self.status = 'on'
            self.bulb.turn_on()
            print("Turning on.")

        try:
            ct = self.mode[mode]['color_temp']
            self.bulb.set_color_temp(ct)
            print(f"Setting mode '{mode}'.")
        except KeyError:
            print("Wrong mode!\nAvailable modes:")
            for mode in self.mode.keys():
                print(f"- {mode}")


if __name__ == "__main__":
    bulb = SmartBulb()

    if len(sys.argv) > 1:
        param = sys.argv[1]
        bulb.set_mode(param)
    else:
        bulb.toggle_power()
