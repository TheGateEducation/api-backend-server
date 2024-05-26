from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
import uuid
from django.utils.translation import gettext_lazy as _
from django.conf import settings
import uuid

class UserManager(BaseUserManager):
    """Custom user manager"""
    def create_user(self, email, password=None, **extra_fields):
        """Create and return a new user"""
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """User object in db"""
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class StudentRecord(models.Model):
    first_contact = models.CharField(max_length=100, blank=True, null=True)
    counsellor = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=100)
    how_did_you_find_us = models.CharField(max_length=255, blank=True, null=True)
    level_of_education = models.CharField(max_length=100)
    level_of_interest = models.CharField(max_length=100)
    area_of_interest = models.CharField(max_length=100)
    program_of_interest = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    country_of_interest = models.CharField(max_length=100)
    intake = models.CharField(max_length=4)
    information = models.CharField(max_length=10, blank=True, null=True)
    documents = models.CharField(max_length=10, blank=True, null=True)
    application = models.CharField(max_length=10, blank=True, null=True)
    offer_letter = models.CharField(max_length=10, blank=True, null=True)
    scholarship = models.TextField(blank=True, null=True)
    acceptance = models.CharField(max_length=10, blank=True, null=True)
    payment = models.CharField(max_length=10, blank=True, null=True)
    coe = models.CharField(max_length=10, blank=True, null=True)
    visa = models.CharField(max_length=10, blank=True, null=True)
    invoice = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    visa_resolution_time = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    total_tuition = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    yearly_tuition = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    commission = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tge = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sales_pax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"
