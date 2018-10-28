from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    url = models.TextField()
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    #Hunter is basically the user that has hunted a project. It will store a user's id number

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]+'...'

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, 20%y')