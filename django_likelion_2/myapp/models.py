from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  email = models.TextField()
  phone_number = models.TextField()
  
  def __str__(self):
    return self.user.username