from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Створення таблиці Topic
class Topic(models.Model):
    text=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.text


# Створення таблиці Note
class Note(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='notes'

    def __str__(self):
        return f"{self.text[:50]}..."
