import math
from .Component import Component

class Component1(Component):
    def __init__(self):
        super(Component1, self).__init__()

        self.attributTypes['url'] = 'string'

    def __str__(self):
        return "Component1"

    def description(self):
        return ""

    def execute(self):
        pass

    def f(self):
        """ Function f() """
