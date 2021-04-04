from thing.thing import Thing


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
    
    def turn_on(self):
        return True

    def turn_off(self):
        return True
