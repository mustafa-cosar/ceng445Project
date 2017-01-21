from .Component import Component
from django.template.response import TemplateResponse

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
        return "Users are able to add topics by giving its name."

    def createHTML(self, request, instanceID):
        context = {}
        return TemplateResponse(request, 'addPost.html', context).render()

    def execute(self):

        result = self['DB'].addPost(self['userName'], self['topicName'], self['postText'])
        if result != None:
            return '<div>Add post is successful</div>'
        else:
            return '<div>Add post is unsuccessful</div>'
