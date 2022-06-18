from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
#from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Specialties(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Patient(User):
    GENDER_CHOICES = (
        ('M', 'ذكر'),
        ('F', 'أنثى'),
    )
    BLOOD_TYPES = (
        ('A+','A+'),
        ('A-','A-'),
        ('B-','B-'),
        ('B+','B+'),
        ('O+','O+'),
        ('O-','O-'),
        ('AB-','AB-'),
        ('AB+','AB+')
    )
    birthday = models.DateField('%Y-%m-%d')
    phone_number = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null=True)
    blood = models.CharField(max_length=50, choices= BLOOD_TYPES)
    city = models.CharField(max_length=50, default='0')

    class Meta:
        verbose_name = _("patient")
        verbose_name_plural = _("patients")
        #abstract = True
    
        def __str__(self):
            return self.username

    def age(self):
        import datetime
        return (datetime.date.today() - self.birthday).days / 365.25


class Doctor(User):
    spcialty = models.ForeignKey(Specialties, on_delete = models.CASCADE)
    work_hours = models.CharField(max_length=100, blank= True , null=True)

    class Meta:
        verbose_name = _("doctor")
        verbose_name_plural = _("doctors")
        #abstract = True

        def __str__(self):
            return self.username

