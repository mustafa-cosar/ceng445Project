from ..Component import Component
from ..Database import Database

class Register(Component):
        def __init__(self):
            super(Login, self).__init__()
            self.attributeTypes["username"] = "string"
            self.attributeTypes["password"] = "string"
            self._DB = Database()

        def __str__(def):
            return "User Login"

        def description(self):
            return "User Login"

        def execute(self):
            uName = self["username"]
            uPwd = self["password"]
            if(self._DB.addUser(uName, uPwd)):
                return "<div> User Added Succesfully! </div>"
            else:
                return "<div> Please Try with Different Username </div>"
