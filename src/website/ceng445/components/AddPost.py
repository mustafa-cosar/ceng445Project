from .Component import Component
from django.template.response import TemplateResponse
from django.http import JsonResponse
from toPickApp.models import Topic

class AddPost(Component):

    def __init__(self):
        super(AddPost, self).__init__()

        self.attributeTypes['topicName'] = 'str'
        self.attributeTypes['userName'] = 'str'
        self.attributeTypes['postText'] = 'str'
        self.attributeTypes['DB'] = 'Database'

    def __str__(self):
        return "AddPost"

    def description(self):
        return "Users are able to add posts."

    def createHTML(self, request, instanceID):
        context = {}
        context['topics'] = Topic.objects.all()
        context['instanceID'] = instanceID
        return TemplateResponse(request, 'addPost.html', context).render()

    def handleAJAXRequest(self, request, instanceID):
        if request.method == 'POST':
            user = request.user
            if not user.is_active:
                raise Exception
            topicID = request.POST.get('topic')
            topic = Topic.objects.get(id=topicID)
            text = request.POST.get('text')

            success = self['DB'].addPost(user, topic, text)

            if success:
                result = {'result': 'success'}
                return JsonResponse(result)
            else:
                raise Exception

    def execute(self):

        result = self['DB'].addPost(self['userName'], self['topicName'], self['postText'])
        if result != None:
            return '<div>Add post is successful</div>'
        else:
            return '<div>Add post is unsuccessful</div>'
