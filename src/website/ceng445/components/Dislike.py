from .Component import Component

class Dislike(Component):

    def __init__(self):
        super(Dislike, self).__init__()

        self.attributeTypes['userName'] = 'str'
        self.attributeTypes['postID'] = 'str'
        self.attributeTypes['DB'] = 'Database'

    def __str__(self):
        return "Dislike"

    def description(self):
        return "User Dislikes a post given a userID and postID"

    def execute(self):

        result = self['DB'].addDislike(self['userName'], self['postID'])

        if result == True:
            return '<div>Dislike successful</div>'
        else:
            return '<div>Dislike unsuccessful</div>'
