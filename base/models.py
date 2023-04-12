from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class List_of_todo(models.Model):
    list_name=models.TextField(max_length=15)
    list_desc=models.TextField(null=True)
    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.list_desc[0:10]



