from thing.thing import Thing


class ColorBrightnessLight(Thing):
    def __init__(self, name, description, color=0, brightness=100):
        super().__init__(name, description)
        self.color = color
        self.type = 'light'
        self.data = {'color': color, 'brightness': brightness}
        # TODO Do the HW thing

    def update(self, data):
        if super().update(data):
            # TODO Do the HW thing
            return True
        return False

    def validate_data(self):
        if not 0 <= self.data['brightness'] <= 100:
            return False
        if not 0 <= self.data['color'] <= 360:
            return False
        return True
