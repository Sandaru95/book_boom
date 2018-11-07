from django.db import models

class Blog_Post(models.Model):
    title = models.CharField(max_length=150)
    main_picture = models.FileField()
    paragraph = models.CharField(max_length=10000)
    posted_on = models.DateTimeField()

    def __str__(self):
        return str(self.title)
