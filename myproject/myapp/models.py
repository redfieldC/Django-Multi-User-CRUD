from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tasks(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField()
  owner = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.title 