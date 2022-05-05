from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Note(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modify = models.DateTimeField(auto_now=True)
    text = models.TextField(blank=True, max_length=10000)

