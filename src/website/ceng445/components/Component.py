import inspect

class Component(object):
    """Component."""

    def __init__(self):
        super(Component, self).__init__()
        self.items = {}
        self.attributeTypes = {}

    def description(self):
        pass

    def createHTML(self, request, instanceID):
        pass

    def handleAJAXRequest(self, request, instanceID):
        pass

    def attributes(self):
        attributeList = []
        for _attr, _type in self.attributeTypes.items():
            attributeList.append((_attr, _type))
        return attributeList

    def __getitem__(self, key):
        return self.items.get(key, None)

    def __setitem__(self, key, value):
        self.items[key] = value

    def methods(self):
        myMethods = inspect.getmembers(self, predicate=inspect.ismethod)
        methodsWithDescriptions = []
        for methodName, value in myMethods:
            desc = inspect.getdoc(getattr(self, methodName))
            if desc != None:
                methodsWithDescriptions.append((methodName, desc))
        return methodsWithDescriptions

    def execute(self):
        pass
