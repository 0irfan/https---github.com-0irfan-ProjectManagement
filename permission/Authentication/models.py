from django.db import models
from django.contrib.auth.models import BaseUserManager


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200,null=False)
    email = models.EmailField(max_length=200,null=False)
    password = models.CharField(max_length=200,null=False)

    
class UserManager(BaseUserManager):
 
    def create_user(self, username, email, password=None):
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
 
        return user
    def create_admin(self, username, email, password=None):
        user = self.create_user(username, email, password)
        user.is_staff = True
 
        user.save()
        return user