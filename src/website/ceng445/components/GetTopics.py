from .Component import Component
from django.template.response import TemplateResponse
from django.http import JsonResponse


class GetTopics(Component):
    def __init__(self):
        super(GetTopics, self).__init__()

    def __str__(self):
        return 'GetTopics'

    def description(self):
        return 'Brings all topics.'

    def handleAJAXRequest(self, request, instanceID):
        if request.method == 'POST':
            result = self['DB'].filterTopics(request)
            return JsonResponse(result)

    def createHTML(self, request, instanceID):
        context = self['DB'].getTopics(request, instanceID)
        return TemplateResponse(request, 'getTopics.html', context).render()
