from ..Component import Component
from ..Database import Database

class Login(Component):
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
            if(self._DB.getUser(uName, uPwd)):
                return "<div> User Login Succesful </div>"
            else:
                return "<div >Bad Username Password Combination </div>"
