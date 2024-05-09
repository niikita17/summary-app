from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.
class Note(models.Model):
    subject_title=models.CharField(max_length=200,null=False )
    title=models.CharField(max_length=200,null=False )
    text=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)