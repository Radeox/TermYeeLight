import sys

import yeelight

from settings import IP


class SmartBulb:
    MODE = {
        "default": {
            "brightness": 66,
            "color_temp": 3000,
        },
        "evening": {
            "brightness": 33,
            "color_temp": 2000,
        },
        "red": {
            "brightness": 10,
            "RGB": (255, 125, 125),
        },
        "work": {
            "brightness": 100,
            "color_temp": 7000,
        },
        "gaming": {
            "brightness": 10,
            "RGB": (0, 0, 255),
        },
    }

    def __init__(self, ip_address):
        self.bulb = yeelight.Bulb(ip_address)
        self.on = self.bulb.get_properties()['power'] == 'on'

    def set_power(self, power):
        if power:
            self.on = True
            self.bulb.turn_on()
        else:
            self.on = False
            self.bulb.turn_off()

    def toggle_power(self):
        self.set_power(not self.on)

    def set_mode(self, mode):
        # If bulb is off, turn it on
        if not self.on:
            self.set_power(True)

        # Set bulb properties
        brightness = self.MODE[mode]['brightness']
        color_temp = self.MODE[mode].get('color_temp')
        self.bulb.set_brightness(brightness)
        rgb = self.MODE[mode].get('RGB')

        if rgb:
            self.bulb.set_rgb(*rgb)
        else:
            self.bulb.set_color_temp(color_temp)


if __name__ == "__main__":
    try:
        bulb = SmartBulb(IP)
    except yeelight.main.BulbException as e:
        print(f"Yee error: {e}")
    else:
        if len(sys.argv) > 1:
            mode = sys.argv[1]

            if mode not in bulb.MODE:
                print("Wrong mode!\nAvailable modes:")
                for mode in bulb.MODE.keys():
                    print(f"- {mode}")
            else:
                print(f"Setting mode '{mode}'.")
                bulb.set_mode(mode)
        else:
            print("Toggling power.")
            bulb.toggle_power()
