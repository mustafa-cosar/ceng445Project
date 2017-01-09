from .Component import Component

class GetPosts(Component):
    def __init__(self):
        super(GetPosts, self).__init__()
        self.attributeTypes['topicName'] = 'str'
        self.attributeTypes['DB'] = 'Database'

    def __str__(self):
        return 'GetPosts'

    def description(self):
        return 'Bring the Posts that are expected by user with topic name.'

    def execute(self):

        result = self['DB'].getPosts(self['topicName'])

        if(result == False):
            return '<div> No Post Found from this Topic </div>'
        else:
            retDiv = ''
            for res in result:
                retDiv = retDiv + '<div>' + res[0] + '</div>'
            return retDiv
