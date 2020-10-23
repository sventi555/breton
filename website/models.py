from django.db import models

# Create your models here.
class Hello(models.Model):
    photo = models.ImageField()
    blurb = models.TextField()

class HelloLink(models.Model):
    title = models.CharField(max_length=128)
    link = models.URLField()
    hello = models.ForeignKey(Hello, related_name='links', on_delete=models.CASCADE)

class Performance(models.Model):
    resume = models.ImageField()

class PerformanceLink(models.Model):
    title = models.CharField(max_length=128)
    link = models.URLField()
    performance = models.ForeignKey(Performance, related_name='links', on_delete=models.CASCADE)
    
class Writing(models.Model):
    credits = models.TextField()

class WritingLink(models.Model):
    title = models.CharField(max_length=128)
    link = models.URLField()
    writing = models.ForeignKey(Writing, related_name='links', on_delete=models.CASCADE)
