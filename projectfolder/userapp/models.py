from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
import uuid

# Create your models here.


class CustomManager(BaseUserManager):

    def create_user(self,email,password = None,**extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        normalized_email = self.normalize_email(email)
        user = self.model(email = normalized_email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email,password=None,**extra_fields):
        user = self.create_user(email,password=password,**extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class GuestUser(AbstractBaseUser):
    user_id = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=255,unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    referral = models.CharField(max_length=50, unique=True)
    own_referral = models.CharField(max_length=50, unique=True)

    # def save(self,*args,**kwargs):
    #     if not self.user_id:
    #         self.user_id = str(uuid.uuid4())[:8]
    #     super().save(*args,**kwargs)

    def save(self):
        if not self.user_id:
            self.user_id = str(uuid.uuid4())[:4]
        super().save()

    
    
    
