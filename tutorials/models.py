from django.db import models
from django.utils import timezone
# Create your models here.
class Tutorial(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    article_name = models.CharField(max_length=100, default='')
    img_name = models.TextField(default='x')

    def __str__(self):
        return self.title