import sys
import time
from yeelight import Bulb
from yeelight.main import BulbException
from settings import IP


class SmartBulb:
    mode = {
        "default": {
            "brightness": 66,
            "color_temp": 3000,
        },
        "evening": {
            "brightness": 33,
            "color_temp": 2000,
        },
        "red": {
            "brightness": 33,
            "RGB": (255, 125, 125),
        },
        "work": {
            "brightness": 100,
            "color_temp": 7000,
        },
        "gaming": {
            "brightness": 20,
            "RGB": (0, 0, 255),
        },
    }

    def __init__(self, ip_address):
        self.bulb = Bulb(ip_address)
        self.status = self.bulb.get_properties()['power']

    def set_power(self, power):
        if power:
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
            for mode in self.mode.keys(): print(f"- {mode}")
            return
        elif self.is_off:
            self.set_power(True)

        brightness = self.mode[mode]['brightness']
        color_temp = self.mode[mode].get('color_temp')
        rgb = self.mode[mode].get('RGB')

        self.bulb.set_brightness(brightness)
        if rgb:
            self.bulb.set_rgb(*rgb)
        else:
            self.bulb.set_color_temp(color_temp)

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
    except BulbException as e:
        print(f"Yee error: {e}")
    else:
        if len(sys.argv) > 1:
            param = sys.argv[1]
            bulb.set_mode(param)
        else:
            bulb.toggle_power()
