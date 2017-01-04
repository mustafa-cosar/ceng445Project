from . import Database

def Singleton(cls):
    _instances = {}
    def getInstance():
        if cls not in _instances:
            _instances[cls] = cls()
        return _instances[cls]
    return getInstance

@Singleton
class Factory:
    def __init__(self):
        self._classes = {}

        self._classes['str'] = str
        self._classes['int'] = int
        self._classes['float'] = float
        self._classes['list'] = list
        self._classes['tuple'] = tuple
        self._classes['dict'] = dict
        self._classes['set'] = set

        self._classes['Database'] = Database.Database

    def createInstance(self,  name, *args, **kwargs):
        try:
            return self._classes[name](*args, **kwargs)
        except:
            return self._classes[name]()
