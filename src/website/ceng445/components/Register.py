from .Component import Component
from django.template.response import TemplateResponse


class Register(Component):
        def __init__(self):
            super(Register, self).__init__()
            self.attributeTypes["username"] = "str"
            self.attributeTypes["password"] = "str"
            self.attributeTypes['DB'] = 'Database'

        def __str__(self):
            return "Register"

        def description(self):
            return "User Register"

        def createHTML(self, request, instanceID):
            return TemplateResponse(request, 'test.html', {}).render()

            # return '''
            # <div>
            #     <form action="/component-{}" method="post">
            #     <input type="textbox" name="username"></input>
            #     <input type="submit">
            #     </form>
            # </div>'''.format(instanceID)

        def execute(self):
            uName = self["username"]
            uPwd = self["password"]
            if(self['DB'].addUser(uName, uPwd)):
                return "<div> User Added Succesfully! </div>"
            else:
                return "<div> Please Try with Different Username </div>"
