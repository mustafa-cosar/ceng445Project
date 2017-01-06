from .Component import Component

class AddTopic(Component):

    def __init__(self):
        super(AddTopic, self).__init__()

        self.attributeTypes['topicName'] = 'str'
        self.attributeTypes['DB'] = 'Database'

    def __str__(self):
        return "AddTopic"

    def description(self):
        return "Users are able to add topics by giving its name."

    def execute(self):

        result = self['DB'].addTopic(self['topicName'])

        if result == True:
            return '<div>Add topic is successful</div>'
        else:
            return '<div>Add topic is unsuccessful</div>'
