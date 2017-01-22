from .Component import Component
from django.template.response import TemplateResponse
from django.http import JsonResponse


class Dislike(Component):

    def __init__(self):
        super(Dislike, self).__init__()

        self.attributeTypes['userName'] = 'str'
        self.attributeTypes['postID'] = 'str'
        self.attributeTypes['DB'] = 'Database'

    def __str__(self):
        return "Dislike"

    def description(self):
        return "User Dislikes a post given a userID and postID"

    def createHTML(self, request, instanceID):
        return TemplateResponse(request, 'dislike.html', {}).render()

    def handleAJAXRequest(self, request):
        if request.method == 'POST':
            result = self['DB'].manageDislike(request)
            return JsonResponse(result)


    def execute(self):

        result = self['DB'].addDislike(self['userName'], self['postID'])

        if result == True:
            return '<div>Dislike successful</div>'
        else:
            return '<div>Dislike unsuccessful</div>'
