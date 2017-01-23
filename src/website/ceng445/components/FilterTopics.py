from .Component import Component
from django.template.response import TemplateResponse
from django.http import JsonResponse


class FilterTopics(Component):
    def __init__(self):
        super(FilterTopics, self).__init__()

    def __str__(self):
        return 'FilterTopics'

    def description(self):
        return 'Bring the Topics according to search name criteria.'

    def handleAJAXRequest(self, request, instanceID):
        if request.method == 'POST':
            result = self['DB'].filterTopics(request)
            return JsonResponse(result)

    def createHTML(self, request, instanceID):
        return TemplateResponse(request, 'filterTopics.html', {}).render()
