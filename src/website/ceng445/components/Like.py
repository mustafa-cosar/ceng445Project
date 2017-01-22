from .Component import Component
from django.template.response import TemplateResponse
from django.http import JsonResponse

class Like(Component):

    def __init__(self):
        super(Like, self).__init__()

        self.attributeTypes['userName'] = 'str'
        self.attributeTypes['postID'] = 'str'
        self.attributeTypes['DB'] = 'Database'

    def __str__(self):
        return "Like"

    def description(self):
        return "User likes a post given a userID and postID"

    def createHTML(self, request, instanceID):
        return TemplateResponse(request, 'like.html', {}).render()

    def handleAJAXRequest(self, request):
        if request.method == 'POST':
            result = self['DB'].manageLike(request)
            return JsonResponse(result)

    def execute(self):

        result = self['DB'].addLike(self['userName'], self['postID'])

        if result == True:
            return '<div>Like successful</div>'
        else:
            return '<div>Like unsuccessful</div>'
