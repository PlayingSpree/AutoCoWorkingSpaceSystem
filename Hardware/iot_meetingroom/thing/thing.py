class Thing:
    current_id = 1

    def __init__(self, name, description):
        self.id = Thing.current_id
        self.name = name
        self.description = description
        self.type = None
        self.data = None

        Thing.current_id += 1

    def update(self, data):
        for key in data:
            if key not in self.data.keys():
                return False
        old_data = self.data.copy()
        self.data.update(data)
        if self.validate_data():
            return True
        self.data = old_data
        return False

    def validate_data(self):
        return True

    def as_dict(self):
        return {'id': self.id,
                'name': self.name,
                'description': self.description,
                'type': self.type,
                'data': self.data}
