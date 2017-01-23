from .Component import Component

class Logout(Component):
        def __init__(self):
            super(Logout, self).__init__()
            self.attributeTypes["username"] = "str"
            self.attributeTypes["password"] = "str"
            self.attributeTypes['DB'] = 'Database'

        def __str__(self):
            return "Logout"

        def description(self):
            return "User Logout"

        def execute(self):
            uName = self["username"]
            uPwd = self["password"]
            if(self['DB'].getUser(uName, uPwd)):
                return "<div> User Login Succesful </div>"
            else:
                return "<div >Bad Username Password Combination </div>"
