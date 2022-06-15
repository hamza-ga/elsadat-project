from django.db import models
from django.urls import reverse

from members.models import Doctor, Patient, Specialties
from django.template.defaultfilters import slugify
import datetime
# Create your models here.

class Consaltations(models.Model):
    category = models.ForeignKey(Specialties,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    disease_symptoms = models.TextField()
    photo = models.ImageField(blank=True, upload_to = 'consultation_image/')

    def __str__(self):
        return str(self.category)

    def get_absolute_url(self):
        #return reverse('post', args = str(self.pk))
        return reverse('sucess')



class Prescription(models.Model):
    doctor_name = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE)
    consult_id = models.ForeignKey(Consaltations, on_delete=models.CASCADE , null= True)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)

    def date_trunc_field(self):
        return self.re_prescription_date.date()

    def __str__(self):
        return str(self.date)

class Appointment(models.Model):
    doc = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    pati = models.ForeignKey(Patient, on_delete=models.CASCADE)
    consultation_id = models.ForeignKey(Consaltations, on_delete=models.CASCADE , null= True)
    date = models.DateField()
    def __str__(self):
        return str(self.date)+ ' ' + str(self.doc)