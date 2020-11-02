class Thing:
    current_id = 1

    def __init__(self, name, description, type, data_info, data):
        self.id = Thing.current_id
        self.name = name
        self.description = description
        self.type = type
        self.data_info = data_info
        self.data = data

        Thing.current_id += 1

    def update(self, data):
        """ Call this before doing the HW thing"""
        for key in data:
            if key not in self.data.keys():
                return False
            if not validator(self.data_info[key], data[key]):
                return False
        self.data.update(data)
        return True

    def as_dict(self):
        return {'id': self.id,
                'name': self.name,
                'description': self.description,
                'type': self.type,
                'data_info': self.data_info,
                'data': self.data}


def validator(data_info, value):
    try:
        if data_info.type == 'integer':
            value = int(value)
        elif data_info.type == 'float':
            value = float(value)
        return data_info.min <= value <= data_info.max
    except:
        return False
