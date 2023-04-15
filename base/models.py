from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Post'
        managed = True
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return str(self.id)