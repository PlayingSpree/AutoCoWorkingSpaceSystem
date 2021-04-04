from thing.thing import Thing
from thing import remote_interface

temp_functions = {17: remote_interface.AC_17,
        18: remote_interface.AC_18,
        19: remote_interface.AC_19,
        20: remote_interface.AC_20,
        21: remote_interface.AC_21,
        22: remote_interface.AC_22,
        23: remote_interface.AC_23,
        24: remote_interface.AC_24,
        25: remote_interface.AC_25,
        26: remote_interface.AC_26,
        27: remote_interface.AC_27,
        28: remote_interface.AC_28,
        29: remote_interface.AC_29,
        30: remote_interface.AC_30}

class Temp(Thing):
    

    def __init__(self, name, description, temp=25, power=False):
        type = 'Temp'
        data_info = {
            'temp': {
                'type': 'integer',
                'min': 17,
                'max': 30
            },
            'power': {
                'type': 'bool'
            }
        }
        data = {'temp': temp,'power': power}

        super().__init__(name, description, type, data_info, data)

    def update(self, data):
        if super().update(data):
            if 'power' not in data or self.data['power']:
                temp_functions[self.data['temp']]()
            else:
                remote_interface.AC_OFF()
            return True
        return False

    def turn_on(self):
        self.update({'power': True})
        return True

    def turn_off(self):
        self.update({'power': False})
        return True
