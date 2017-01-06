from .Component import Component

class GetPosts(Component):
    def __init__(self):
        super(GetPosts, self).__init__()


    def __str__(self):
        return 'GetPosts'

    def description(self):
        return 'Bring the Posts that are related with the Topics the User is following'

    def execute(self):
        #TODO Implement GetPosts
        return ''
