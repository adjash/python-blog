import datetime
from django.db import models
from django.utils import timezone
# Create your models here. You can actually create methods within the models
class BlogPost(models.Model):
    blog_title = models.CharField(max_length=20)
    blog_content = models.CharField(max_length=500, default='something went wrong :(')
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=50)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    
    def __str__(self):
        return self.blog_title