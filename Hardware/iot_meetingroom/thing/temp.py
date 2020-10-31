from thing.thing import Thing


class Temp(Thing):
    def __init__(self, name, description, temp=25):
        type = 'Temp'
        data_info = [{'key': 'temp',
                      'type': 'integer',
                      'min': 20,
                      'max': 30}]
        data = {'temp': temp}
        super().__init__(name, description, type, data_info, data)

    def update(self, data):
        if super().update(data):
            # TODO Do the HW thing
            return True
        return False
