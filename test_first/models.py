from django.db import models
from django.utils import timezone


# Create models..


class User(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Post(models.Model):
    title = models.CharField(max_length=255, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.text
