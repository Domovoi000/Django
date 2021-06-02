from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%y/%m/%d')

    def __str__(self):
        return self.title
