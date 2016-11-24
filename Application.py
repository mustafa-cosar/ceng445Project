import os
import uuid
from . import components

class Application(object):
    """Application."""

    def __init__(self):
        super(Application, self).__init__()
        self._componentsModule = components
        self._loadedComponents = {}
        self._instances = {}

    def available(self):
        return self._componentsModule.__all__

    def loaded(self):
        retDic = {}
        for cName, compFunc in self._loadedComponents.items():
            retDic[cName] = compFunc().description()
        return retDic

    def load(self,  name):
        if name not in self._loadedComponents.keys():
            self._loadedComponents[name] = getattr(self._componentsModule, name)

    def loadDesign(self,  path):
        pass

    def saveDesign(self,  path):
        pass

    def addInstance(self,  componentName, x, y):
        instanceID = str(uuid.uuid4())
        self._instances[instanceID] = (self._loadedComponents[componentName](), x, y)
        return instanceID

    def instances(self):
        return self._instances

    def removeInstance(self, id):
        del self._instances[id]

    def callMethod(self,  id, methodName, *params):
        if params == (None,):
            return getattr(self._instances[id][0], methodName)()
        else:
            return getattr(self._instances[id][0], methodName)(*params)

    def execute(self):
        totalResult = ''

        for comp in self.instances.values():
            totalResult += comp.execute()

        return '<html>' + totalResult + '</html>'
