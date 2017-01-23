from .Component import Component
from django.template.response import TemplateResponse
from django.http import JsonResponse


class FollowTopic(Component):
    def __init__(self):
        super(FollowTopic, self).__init__()

    def __str__(self):
        return 'FollowTopic'

    def description(self):
        return 'Make user to follow topics whichever they like.'

    def handleAJAXRequest(self, request, instanceID):
        if request.method == 'POST':
            result = self['DB'].followTopic(request)
            return JsonResponse(result)

    def createHTML(self, request, instanceID):
        return TemplateResponse(request, 'getTopics.html', {}).render()
