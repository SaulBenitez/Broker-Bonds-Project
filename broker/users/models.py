from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    '''
    Manager for user 
    '''

    def create_user(self, email, fullname, username, password):
        ''' 
        Create and save a new user 
        '''
        if not email:
            raise ValueError('User must enter an e-mail adderess')

        if not username:
            raise ValueError('User must enter a username')

        email = self.normalize_email(email)
        user = self.model(fullname=fullname, email=email, username=username)
        
        user.set_password(password)
        user.save(using=self._db) 

        return user

    def create_superuser(self, email, fullname, username, password):
        '''
        Create and save a new superuser with given details 
        '''
        user = self.create_user(email, fullname, username, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    ''' 
    Databases model for users in the system 
    '''
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50, unique=True)
    # created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    # Replace the username field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname', 'username']

    def get_full_name(self):
        ''' Retrieve full name of user '''
        return self.fullname

    def get_short_name(self):
        ''' Retrieve short name of user '''
        return self.username

    def __str__(self):
        ''' Return string representation of our user'''
        return "{}, ({})".format(self.fullname, self.email)
        #return self.email


