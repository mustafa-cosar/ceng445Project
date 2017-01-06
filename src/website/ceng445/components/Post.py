from .Component import Component

class Post(Component):
    def __init__(self):
        super(Post, self).__init__()
        self.attributeTypes['user'] = 'str'
        self.attributeTypes['content'] = 'str'
        self.attributeTypes['DB'] = 'Database'


    def __str__(self):
        return 'Post'

    def description(self):
        return 'User posts something related to some topics'

    def execute(self):
        #TODO Implement posting something
        return ''
