from thing.thing import Thing


class ColorBrightnessLight(Thing):
    def __init__(self, name, description, color=0, brightness=100):
        type = 'ColorBrightnessLight'
        data_info = {
            'color': {
                'type': 'float',
                'min': 0,
                'max': 100
            },
            'brightness': {
                'type': 'float',
                'min': 0,
                'max': 100
            }
        }
        data = {'color': color, 'brightness': brightness}
        super().__init__(name, description, type, data_info, data)
