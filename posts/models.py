from django.db import models
from categories.models import Category
from author.models import Author
# Create your models here.
class Post(models.Model):
    tittle = models.CharField(max_length=40)
    content = models.TextField()
    categori = models.ManyToManyField(Category)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)# all delete
    # author = models.ForeignKey(Author,on_delete=models.SET_DEFAULT)# profile delete but post show

    def __str__(self):
        return self.tittle