from django.db import models

# Create your models here.
# Reporter(1) - Article(N)
# reporter - name

class Reporter(models.Model):
    name = models.CharField(max_length=10)

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    image = models.ImageField()
    
# Article(1) - Comment(N)
# comment - content
class Comment(models.Model):
    content = models.CharField(max_length=10)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

class Question(models.Model):
    title = models.CharField(max_length=10)

class Choice(models.Model):
    content = models.CharField(max_length=10)
    votes = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

