from .Component import Component
from django.template.response import TemplateResponse
from django.shortcuts import render
from django.http import JsonResponse


class GetPosts(Component):
    def __init__(self):
        super(GetPosts, self).__init__()
        self.attributeTypes['topicName'] = 'str'
        self.attributeTypes['DB'] = 'Database'

    def __str__(self):
        return 'GetPosts'

    def description(self):
        return 'Brings the Posts that are followed by user with topic name.'

    def createHTML(self, request, instanceID):
        context = self['DB'].getPosts(request, instanceID)
        return TemplateResponse(request, 'getPosts.html', context).render()

    def handleAJAXRequest(self, request, instanceID):
        context = self['DB'].getPosts(request, instanceID)
        print(context)
        return render(request, 'getPosts-postList.html', context)

    def execute(self):

        result = self['DB'].getPosts(self['topicName'])

        if(result == False):
            return '<div> No Post Found from this Topic </div>'
        else:
            retDiv = ''
            for res in result:
                retDiv = retDiv + '<div>' + res[0] + '</div>'
            return retDiv
