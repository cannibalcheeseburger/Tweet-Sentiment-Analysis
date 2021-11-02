from django.db import models

# Create your models here.


class tweet(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.TextField()
    date = models.CharField(max_length=100)
    flag = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    target = models.IntegerField()

    def __str__(self):
        return str(self.id)

