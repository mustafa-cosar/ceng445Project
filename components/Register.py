from .Component import Component

class Register(Component):
        def __init__(self):
            super(Register, self).__init__()
            self.attributeTypes["username"] = "string"
            self.attributeTypes["password"] = "string"
            self.attributeTypes['DB'] = 'database'

        def __str__(self):
            return "User Register"

        def description(self):
            return "User Register"

        def execute(self):
            uName = self["username"]
            uPwd = self["password"]
            if(self['DB'].addUser(uName, uPwd)):
                return "<div> User Added Succesfully! </div>"
            else:
                return "<div> Please Try with Different Username </div>"
