from .Component import Component

class Login(Component):
        def __init__(self):
            super(Login, self).__init__()
            self.attributeTypes["username"] = "str"
            self.attributeTypes["password"] = "str"
            self.attributeTypes['DB'] = 'Database'

        def __str__(self):
            return "Login"

        def description(self):
            return "User Login"

        def execute(self):
            uName = self["username"]
            uPwd = self["password"]
            if(self['DB'].getUser(uName, uPwd)):
                return "<div> User Login Succesful </div>"
            else:
                return "<div >Bad Username Password Combination </div>"
