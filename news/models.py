from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150)
    main_picture = models.FileField()
    paragraph = models.CharField(max_length=500)
    posted_on = models.DateTimeField()

    def __str__(self):
        return str(self.title)
