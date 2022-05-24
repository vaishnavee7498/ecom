from django.contrib.auth.models import UserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(unique=True)
    address = models.TextField()
    dob = models.DateField(null=True)
    company = models.CharField(max_length=55)
    mobile = models.IntegerField(
        help_text='Must include international prefix - e.g. +1 555 555 55555', )
    city = models.CharField(max_length=55, null=True, blank=True)
    is_hr = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_employee = models.BooleanField(default=False)
    employee_id = models.CharField(max_length=20)

    #
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    #
    # objects = UserManager()
class Product(models.Model):
    productname = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.CharField(max_length=5000, null=True, blank=True)

class recommondation(models.Model):
    user_id = models.CharField(max_length=10, null=True)
    product_id = models.CharField(max_length=10, null=True)