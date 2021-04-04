from thing.thing import Thing
from thing import remote_interface

class ColorBrightnessLight(Thing):
    def __init__(self, name, description):
        type = 'ColorBrightnessLight'
        data_info = {
            'brightness_up': {
                'type': 'bool',
            },
            'brightness_down': {
                'type': 'bool',
            },
            'power': {
                'type': 'bool',
            }
        }
        data = {'power': False, 'brightness_up': False,'brightness_down': False}
        super().__init__(name, description, type, data_info, data)

    def update(self, data):
        if super().update(data):
            if 'power' in data:
                if data['power']:
                    remote_interface.LED_ON()
                else:
                    remote_interface.LED_OFF()
            if 'brightness_up' in data and data['brightness_up']:
                remote_interface.LED_UP()
            if 'brightness_down' in data and data['brightness_down']:
                remote_interface.LED_DOWN()
            return True
        return False
    
    def turn_on(self):
        self.update({'power': True})
        return True

    def turn_off(self):
        self.update({'power': False})
        return True
