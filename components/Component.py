class Component(object):
    """Component."""

    def __init__(self):
        super(Component, self).__init__()
        self.items = {}
        self.attributeTypes = {}


    def description(self):
        pass

    def attributes(self):
        attributeList = []
        for _attr, _type in self.attributeTypes.items():
            attributeList.append((_attr, _type))
        return attributeList

    def __getitem__(self, key):
        return self.items[key]

    def __setitem__(self, key, value):
        self.items[key] = value

    def methods(self):
        pass

    def execute(self):
        pass
