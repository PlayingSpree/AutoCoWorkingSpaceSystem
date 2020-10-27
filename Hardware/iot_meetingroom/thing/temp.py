from thing.thing import Thing


class Temp(Thing):
    def __init__(self, name, description, temp=25):
        super().__init__(name, description)
        self.type = 'Temp'
        self.data = {'temp': temp}
        # TODO Do the HW thing

    def update(self, data):
        if super().update(data):
            # TODO Do the HW thing
            return True
        return False

    def validate_data(self):
        if not 20 <= self.data['temp'] <= 30:
            return False
        return True
