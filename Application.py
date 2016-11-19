import os
import importlib
import uuid

class Application(object):
    """Application."""

    _componentPath = "components"

    def __init__(self):
        super(Application, self).__init__()
        self._componentsModule = importlib.__import__(Application._componentPath)
        self._loadedComponents = {}
        self._instances = {}

    def available(self):
        return self.componentsModule.__all__

    def loaded(self):
        retDic = {}
        for cName, compFunc in self._loadedComponents:
            retDic[cName] = compFunc.description()
        return retDic

    def load(self,  name):
        if name not in self._loadedComponents.keys():
            self._loadedComponents[name] = importlib.import_module('.' + name, Application._componentPath)

    def loadDesign(self,  path):
        pass

    def saveDesign(self,  path):
        pass

    def addInstance(self,  componentName, x, y):
        instanceID = str(uuid.uuid4())
        self._instances[instanceID] = (getattr(self._loadedComponents[componentName], componentName)(), x, y)
        return instanceID

    def instances(self):
        return self._instances

    def removeInstance(self, id):
        del self._instances[id]

    def callMethod(self,  id, methodName, *params):
        getattr(self._instances[id],methodName)(params)

    def execute(self):
        pass
