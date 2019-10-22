from django.db import models
# Create your models here.
class User(models.Model):
    username = models.TextField()

class Article(models.Model):
    title = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)