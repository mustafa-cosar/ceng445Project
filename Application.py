class Application(object):
    """Application."""
    def __init__(self, arg):
        super(Application, self).__init__()
        self.arg = arg


    def available(self):
        pass

    def loaded(self):
        pass

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
