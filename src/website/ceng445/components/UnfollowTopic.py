from .Component import Component

class UnfollowTopic(Component):
    def __init__(self):
        super(UnfollowTopic, self).__init__()


    def __str__(self):
        return 'UnfollowTopic'

    def description(self):
        return 'User unfollows a Topic.'

    def execute(self):
        #TODO Implement UnfollowTopic
        return ''
