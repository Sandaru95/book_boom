from django.db import models
from django.contrib.auth.models import User
from blog.models import Blog_Post


class Comment(models.Model):
    post = models.ForeignKey(Blog_Post, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)

    def __str__(self):
        return str(self.owner) + ' - ' + str(self.comment)

