from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_id = models.AutoField(primary_key = True)
    topic_name = models.CharField('Topic Name' ,max_lenght = 256, unique = True)

class Post(models.Model):
    post_id = models.AutoField(primary_key = True)
    post_text = models.CharField('Post Name' ,max_lenght = 512)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    topic_id = models.ForeignKey(Topic, on_delete = models.CASCADE)
    post_date = models.DateTimeField('Post Date')

class Like(models.Model):
    liking_user = models.ForeignKey(User, on_delete = models.CASCADE)
    liked_post = models.ForeignKey(Post, on_delete = models.CASCADE)
    class Meta:
        unique_together = ('liking_user','liked_post')

class Dislike(models.Model):
    disliking_user = models.ForeignKey(User, on_delete = models.CASCADE)
    disliked_post = models.ForeignKey(Post, on_delete = models.CASCADE)
    class Meta:
        unique_together = ('disliking_user','disliked_post')
