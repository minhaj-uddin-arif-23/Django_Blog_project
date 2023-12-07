from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    phone_no = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name