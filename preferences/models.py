from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractUser
)

class Client(models.Model):
  readonly_fields = ("created_at", "updated_at")
  name = models.CharField(max_length=40, null=False, blank=False)
  phone = models.CharField(max_length=40, null=False, blank=False)
  email = models.CharField(max_length=40)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """

    def create_user(self, email, password=None):
        """
        Creates and saves a user with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user 

class User(AbstractUser):
  USER_ROLES = [
    ('admin', 'ADMIN'),
    ('user', 'USER'),
    # Add more roles here
  ]
  class Meta:
    verbose_name = "User"
    verbose_name_plural = "Users"
    ordering = ["-created_at"]
  
  readonly_fields = ("created_at", "updated_at")
  username = models.CharField(unique=True,max_length=30)
  email = models.EmailField(
      verbose_name='email address',
      max_length=255,
      unique=True,
  )
  role = models.CharField(max_length=40, choices=USER_ROLES, default='user', null=False, blank=False)
  client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True, related_name='users')

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = UserManager()

  def __str__(self):
      return self.email

class Preferences(models.Model):
    readonly_fields = ("created_at", "updated_at")
    client = models.ForeignKey(Client,related_name='preferences',  on_delete=models.CASCADE)
    key = models.CharField(max_length=40, null=False, blank=False)
    value = models.CharField(max_length=250, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.key
    
    class Meta:
        verbose_name = "Preference"
        verbose_name_plural = "Preferences"
        ordering = ["-created_at"]