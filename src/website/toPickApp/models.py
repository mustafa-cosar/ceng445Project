from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField('Topic Name' ,max_length = 256, unique = True)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.name)

class Post(models.Model):
    text = models.TextField('Post Text' ,max_length = 512)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    date = models.DateTimeField('Post Date', auto_now_add=True)
    liking_users = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    disliking_users = models.ManyToManyField(User, related_name='disliked_posts', blank=True)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.text)[:30]


#
# ########## Below this line may be unnecessary
#
# class Like(models.Model):
#     liking_user = models.ForeignKey(User, on_delete = models.CASCADE)
#     liked_post = models.ForeignKey(Post, on_delete = models.CASCADE)
#     class Meta:
#         unique_together = ('liking_user','liked_post')
#
# class Dislike(models.Model):
#     disliking_user = models.ForeignKey(User, on_delete = models.CASCADE)
#     disliked_post = models.ForeignKey(Post, on_delete = models.CASCADE)
#     class Meta:
#         unique_together = ('disliking_user','disliked_post')
