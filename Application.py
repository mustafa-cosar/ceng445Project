import os

class Application(object):

    _componentPath = "components/"

    """Application."""
    def __init__(self):
        super(Application, self).__init__()

        self._loadedComponents = {}


    def available(self):
        pass

    def loaded(self):
        return self._loadedComponents

    def load(self):
        pass

    def loadDesign(self, path):
        pass

    def saveDesign(self, path):
        pass

    def addInstance(self, componentName, x, y):
        pass

    def instances(self):
        pass

    def removeInstance(self, id):
        pass

    def callMethod(self, id, methodName, *params):
        pass

    def execute(self):
        pass
