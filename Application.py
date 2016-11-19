import os
import importlib

class Application(object):
    """Application."""

    _componentPath = "components"

    def __init__(self):
        super(Application, self).__init__()
        self.componontsModule = importlib.__import__(Application._componentPath)

        self._loadedComponents = {}


    def available(self):
        pass

    def loaded(self):

    def load(self,  name):
        if name not in self._loadedComponents.keys():
            self._loadedComponents[name] = importlib.import_module('.' + name, Application._componentPath)

    def loadDesign(self,  path):
        pass

    def saveDesign(self,  path):
        pass

    def addInstance(self,  componentName, x, y):
        pass

    def instances(self):
        pass

    def removeInstance(self,  id):
        pass

    def callMethod(self,  id, methodName, *params):
        pass

    def execute(self):
        pass
