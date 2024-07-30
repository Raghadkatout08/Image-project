from django.db import models

# Create your models here.
class Food(models.Model):
    id = models.BigIntegerField(primary_key=True)
    largeImageURL = models.CharField(max_length=900)
    tags = models.CharField(max_length=200)
    views = models.IntegerField()
    downloads = models.IntegerField()
    collections = models.IntegerField()
    likes = models.IntegerField()
    comments = models.IntegerField()
    user = models.CharField(max_length=100)
    userImageURL = models.CharField(max_length=800, null=True, blank=True)

    def __str__(self):
        return self.tags