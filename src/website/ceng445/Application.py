import os
import sys
import uuid
import json
from . import components
from . import Database
from . import Factory

class Application(object):
    """Application."""

    def __init__(self):
        super(Application, self).__init__()
        self._componentsModule = components
        self._loadedComponents = {}
        self._instances = {}

    def available(self):
        return self._componentsModule.__all__

    def _isAvailable(self,  name):
        return name in self.available()

    def loaded(self):
        retDic = {}
        for cName, compFunc in self._loadedComponents.items():
            retDic[cName] = compFunc().description()
        return retDic

    def _isLoaded(self,  name):
        return name in self._loadedComponents.keys()

    def load(self,  name):
        if name in self.available() and name not in self._loadedComponents.keys():
            self._loadedComponents[name] = getattr(self._componentsModule, name)
            return True
        return False

    def loadDesign(self,  path):
        design = None
        if path:
            with open(path, 'r') as fp:
                design = json.load(fp)
        if design:
            self._loadState(design)

    def _loadState(self, design):

        self.__init__()

        for i in design['loaded']:
            self.load(i)

        for i in design['instances']:
            ID = self.addInstance(i['instanceName'], i['x'], i['y'])
            instance = self._instances[ID]
            del self._instances[ID]
            self._instances[i.get('instanceID', ID)] = instance
            ID = i.get('instanceID', ID)
            attributeTypes = dict(self.callMethod(ID, 'attributes', None))
            for attributeName, value in i['attributes'].items():
                attributeType = attributeTypes[attributeName]
                attributeValue = Factory.Factory().createInstance(attributeType, value)

                self.callMethod(ID, '__setitem__', attributeName, attributeValue)

    def saveDesign(self,  path):
        design = self._dumpState()

        if path:
            with open(path, 'w') as fp:
                json.dump(design, fp, indent='\t')

    def _dumpState(self):
        design = {'instances':[], 'loaded': list(self._loadedComponents.keys())}
        for instanceID, (instance, x, y) in list(self._instances.items()):
            instanceAttributes = dict([(name[0], str(instance[name[0]])) for name in list(instance.attributes())])
            instanceObj = {'instanceID': instanceID,'instanceName': str(instance), 'x':x, 'y':y, 'attributes': instanceAttributes}
            design['instances'].append(instanceObj)
        return design

    def __getstate__(self):
        return (self._dumpState(), )

    def __setstate__(self, state):
        self._loadState(state[0])

    def addInstance(self,  componentName, x, y):
        instanceID = str(uuid.uuid4())
        instance = self._loadedComponents[componentName]()
        instance['DB'] = Factory.Factory().createInstance('Database')
        self._instances[instanceID] = (instance, x, y)
        return instanceID

    def instances(self):
        retVal = {}
        for key, val in self._instances.items():
            retVal[key] = (str(val[0]), val[1], val[2])
        return retVal

    def removeInstance(self,  id):
        if self._instances.get(id, False):
            del self._instances[id]

    def callMethod(self,  id, methodName, *params):
        if params == (None,):
            return getattr(self._instances[id][0], methodName)()
        else:
            return getattr(self._instances[id][0], methodName)(*params)

    def execute(self):
        x, y = self._findMaxGridXY()
        grid = self._makeGrid(x+1, y+1)

        for ID, comp in self._instances.items():
            ins, x, y = comp
            grid[x][y] = ins

        totalResult = ''

        for i in grid:
            totalResult += '<div>'
            for j in i:
                totalResult += self._executeInstance(j)
            totalResult += '</div>'

        return '<!DOCTYPE HTML>\n<html> <head></head><body>' + totalResult + '</body></html>'

    def _executeInstance(self,  instance):
        if instance == None:
            return '<div></div>'
        else:
            return '<div>' + instance.execute() + '</div>'

    def _findMaxGridXY(self):
        x, y = 0, 0

        for instance, instanceX, instanceY in list(self._instances.values()):
            if instanceX > x:
                x = instanceX
            if instanceY > y:
                y = instanceY
        return (x, y)

    def _makeGrid(self,  x, y):
        return [[None for j in range(y)] for i in range(x)]


    def makeGridHTML(self, request):
        x, y = self._findMaxGridXY()
        grid = self._makeGrid(x+1, y+1)

        for ID, comp in self._instances.items():
            ins, x, y = comp
            grid[x][y] = ins.createHTML(request, ID)

        return grid
