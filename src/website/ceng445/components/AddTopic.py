from .Component import Component
from django.template.response import TemplateResponse
from django.http import JsonResponse

class AddTopic(Component):

    def __init__(self):
        super(AddTopic, self).__init__()

        self.attributeTypes['topicName'] = 'str'
        self.attributeTypes['DB'] = 'Database'

    def __str__(self):
        return "AddTopic"

    def description(self):
        return "Users are able to add topics by giving its name."

    def createHTML(self, request, instanceID):
        context = {}
        context['instanceID'] = instanceID
        return TemplateResponse(request, 'addTopic.html', context).render()

    def handleAJAXRequest(self, request, instanceID):

        if request.method == 'POST':
            topicName = request.POST.get('topicName', None)

            success = self['DB'].addTopic(topicName)
            if success:
                return JsonResponse({'result': 'success'})
            else:
                raise Exception

    def execute(self):

        result = self['DB'].addTopic(self['topicName'])

        if result != None:
            return '<div>Add topic is successful</div>'
        else:
            return '<div>Add topic is unsuccessful</div>'
