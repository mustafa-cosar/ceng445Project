from ..Component import Component

class Login(Component):
        def __init__(self):
            super(Login, self).__init__()
            self.attributeTypes["usename"] = "string"
            self.attributeTypes["password"] = "string"

        def __str__(def):
            return "User Login"

        def description(self):
            return "User Login"

        def execute(self):
            pass
